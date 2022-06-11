#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "protocol.h"
#include "datalink.h"

void printData(char *p, int size);

typedef unsigned char seq_nr;
typedef unsigned char frame_kind;
typedef struct{unsigned char data[PKT_LEN];} packet;
typedef enum{network_layer_ready, physical_layer_ready, frame_arrive, data_timout, ack_timeout, chksum_error} event_type;
typedef enum{F, T} mybool;

typedef struct
{
    frame_kind kind; /* FRAME_DATA */
    seq_nr ack;
    seq_nr seq;
    packet info;	/* packet */
	unsigned char padding[4];	/* memory space used for crc code, 32 bit */
} frame;

mybool no_nak = T; /* no nak has beem yet */


static void Inc(seq_nr *seq)
{
	*seq = (*seq + 1) % (MAX_SEQ + 1);
}


static mybool between(seq_nr a, seq_nr b, seq_nr c)
{
    /*return T if a <= b circulaly; F otherwise*/
    return ((a <= b) && (b < c)) || ((c < a) && (a <= b)) || ((b < c) && (c < a));
}


static void send(frame_kind fk, seq_nr frame_nr, seq_nr frame_expected, packet buf[])
{
    /* construct frame and send */
    frame s; /* tmp variable */
    s.kind = fk; /* s.kind  = data/ack/nak */

	if (fk == FRAME_DATA)
		memcpy((char*)&s.info, (char*)&buf[frame_nr % NR_BUFS], PKT_LEN);	/* store the packet */
	
    s.seq = frame_nr; /* only meaning for data */
    s.ack = (frame_expected + MAX_SEQ) % (MAX_SEQ + 1);

	if (fk == FRAME_NAK)
        no_nak = F;

	/* compute the crc code, the crc code is in the padding memory */
	*(unsigned int*) ((unsigned char*)&s + PKT_LEN + 3) = crc32((unsigned char*)&s, PKT_LEN + 3);

	/* send the frame to the physical layer */
	send_frame((unsigned char*)&s, sizeof(s));

	dbg_event("组装之后的 !!\n");
	printData((char*)&s, sizeof(s));

	//printf("CRC send");
	//printData(s.padding,4);
	/* warning: short may not be 2 bytes, according to the computer */
	if (fk == FRAME_DATA)
		dbg_frame("Send DATA seq:%d ack:%d, ID %d\n", s.seq, s.ack, *(short *)(&s.info));
	else if (fk == FRAME_ACK)
		dbg_frame("Send ACK seq:%d\n", s.seq);
	else if (fk == FRAME_NAK)
		dbg_frame("Send NAK seq:%d\n", s.seq);

	if (fk == FRAME_DATA)	/* start the timeout, if timeout,  repeat transmit */
		start_timer(frame_nr % NR_BUFS, DATA_TIMER);

    stop_ack_timer(); /* no need for separate ack frame */
}


void protocol6()
{
	int mid,stop=0;
    seq_nr ack_expected = 0;	/* lower edge of sender's window */
    seq_nr next_frame_to_send = 0;	/* upper edge of sender's window */
    seq_nr frame_expected = 0;	/* lower edge of receiver's window */
	seq_nr too_far = NR_BUFS;	/* uppder edge receiver's window + 1*/
    
    packet out_buf[NR_BUFS];    /* buffers for the outbound stream*/
    packet in_buf[NR_BUFS];    /* buffers for the inbound stream*/
	mybool arrived[NR_BUFS] = {F};	/* inbound bit map, intial to all F */
    seq_nr nbuffered = 0;	/* the size of buffered */

	frame r;	/* tmp variable */
    int arg = MAX_SEQ + 1; /* para */
    int len = 0; /* the length of received packet*/
	unsigned crc_ret = 0;
	event_type event; /* type of event */
	
	enable_network_layer();
	
    while (T)
    {
		event = (event_type)wait_for_event(&arg);	/* event to be what */
        switch (event)
        {
		case network_layer_ready:	/* accept, save, and transmit a new frame;sender */
			dbg_event("network_layer_ready; \n");
            ++nbuffered;	/* expand the window */	
			get_packet((unsigned char*)&out_buf[next_frame_to_send % NR_BUFS]);	/* fetch new packet int the window */
			
			dbg_event("从网络层来的 !!\n");
        	printData((char*)&out_buf[next_frame_to_send % NR_BUFS], sizeof(out_buf[next_frame_to_send % NR_BUFS]));

			send(FRAME_DATA, next_frame_to_send, frame_expected, out_buf);	/* transmit the new frame */
									
			
			Inc(&next_frame_to_send);	/* advance the upper window edge */
            break;
		
		case frame_arrive:	/* a data or control frame has arrived */
			dbg_event("\nframe_arrival; \n");
			/* fetch incoming frame from physical layer, len get the size of the recevied frame */
				
			
			len = recv_frame((unsigned char*)&r, sizeof(r));
			
			dbg_event("从链路层收来的 !!\n");
			printData((char*)&r, sizeof(r));
			/* warning: short may not be 2 bytes, according to the computer */
			if (r.kind == FRAME_DATA)
				dbg_frame("Recv DATA seq:%d ack:%d, ID %d\n", r.seq, r.ack, *(short *)(&r.info));
			else if (r.kind == FRAME_ACK)
				dbg_frame("Recv ACK seq:%d\n", r.seq);
			else if (r.kind == FRAME_NAK)
				dbg_frame("Recv NAK seq:%d\n", r.seq);
			
			//dbg_frame("CRC receive:");
			//printData(r.padding,4);//打印CRC
			
			if (r.kind == FRAME_DATA)		/* if it's a data frame, check seq and whether it should be received */
            {
				/* check the crc code */
				crc_ret = crc32((unsigned char*)&r, len);
				if (crc_ret != 0)	/* check crc code error, goto chksum_error */
				{
					goto crc_error;
				}
									
				//printf("crc correct!\n");
				/* an undamage frame has arrived*/
                if (r.seq != frame_expected && no_nak)	/* it's not the expected frame, send back a nak frame */
                {
					send(FRAME_NAK, 0, frame_expected, out_buf);	/* send nak, 0 has no meanings */
                }
                else
                {
					start_ack_timer(ACK_TIMER);	/* right frame, start the ack timer, whether to send back ack by a sepatate frame */
                }

				/* the receiver's window */
                if (between(frame_expected, r.seq, too_far) && arrived[r.seq % NR_BUFS] == F)	/* in the window and has't ever arrived */
                {
					/* frame may be received in any order */
                    arrived[r.seq % NR_BUFS] = T;	/* record in the bit map the arrival of some frame */
					memcpy(&in_buf[r.seq % NR_BUFS], &r.info, sizeof(packet));    /* store the frame */
                    while (arrived[frame_expected % NR_BUFS])	/* the expected frame has successfully arrived, welcome it */
                    {
						/* pass the frame and advance the window */
						put_packet((unsigned char*)&in_buf[frame_expected % NR_BUFS], sizeof(packet));
						//dbg_frame("RIGHT RECEIVE！　Recv DATA %d %d, ID %d\n", frame_expected % NR_BUFS, r.ack, *(short *)(&r.info));
						/* clear the state variable */
                        no_nak = T;
                        arrived[frame_expected % NR_BUFS] = F;

						Inc(&frame_expected);	/* update the expected frame */
						Inc(&too_far);	/* advance the window */

						start_ack_timer(ACK_TIMER);	/* to see if a separate ack is needed */
                    }
                }
				/* this code has two start_ack_timer(), again will not reset */
            }

			/* selective retransmit */
			if (r.kind == FRAME_NAK && between(ack_expected, (seq_nr)((r.ack + 1) % (MAX_SEQ + 1)), next_frame_to_send))
				send(FRAME_DATA, (seq_nr)((r.ack + 1) % (MAX_SEQ + 1)), frame_expected, out_buf);

	/*		if(*(short *)(&r.info)==20007)
			{
				scanf("%d",&mid);
				stop=1;
			}
*/
			/* check the confirm seq, if it has been received successfully, advance the sender's window */
            while (between(ack_expected, r.ack, next_frame_to_send))
            {
                --nbuffered;	/* handle piggbacked ack */
                stop_timer(ack_expected % NR_BUFS);	/* frame arrived intact */
				Inc(&ack_expected);	/* advance the sender's window */
            }
            break;

		case data_timout:	/* timeout retransmit */
			dbg_event("\ndata_timout; \n");
			/* arg hold the seq of the timeout timer */
			send(FRAME_DATA, (seq_nr)arg, frame_expected, out_buf);
			dbg_event("arg=%d; \n",arg);
            break;
            
		case ack_timeout:
			dbg_event("\nack_timout; \n");
			send(FRAME_ACK, 0, frame_expected, out_buf);    /* ack timeout, send ack */
            break;
            
		case chksum_error:	/* damaged frame */
crc_error:	dbg_event("checksum_error; \n");
			if (no_nak)
			{
				send(FRAME_NAK, 0, frame_expected, out_buf);	/* damaged frame */
			}
			break;

        default:
            break;

	//	scanf("%d",&mid);
        }
		printf("\n");
		if (nbuffered < NR_BUFS)	
			enable_network_layer();
		else	
			disable_network_layer();
	}
}


int main(int argc, char* argv[])
{
	protocol_init(argc, argv);
    lprintf("Designed by Duan Yibo, build: " __DATE__"  "__TIME__"\n");
    protocol6();

	return 0;
}


void printData(char *p, int size)
{
	int i = 0;
	for (i = 0; i <= size - 1; ++i)
	{
		//printf("%x", p[i]);
		dbg_event("%x", p[i]);
	}
	dbg_event("\n");
}


