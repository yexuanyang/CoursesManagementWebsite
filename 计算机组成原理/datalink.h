
/* FRAME kind, less than 255*/
#define FRAME_DATA 1
#define FRAME_ACK  2
#define FRAME_NAK  3

/* addition for event type, less than 255 */
#define CKSUM_ERROR 5

/* data frame timout max time */
#define DATA_TIMER  800

/* ack frame timeout max time*/
#define ACK_TIMER 200

/* the max seq of frame */
#define MAX_SEQ 7

/* the receiver's windows buffer size */
#define NR_BUFS ((MAX_SEQ + 1) / 2)

/*  
    DATA Frame
    +=========+========+========+===============+========+
    | KIND(1) | SEQ(1) | ACK(1) | DATA(240~256) | CRC(4) |
    +=========+========+========+===============+========+

    ACK Frame
    +=========+========+========+
    | KIND(1) | ACK(1) | CRC(4) |
    +=========+========+========+

    NAK Frame
    +=========+========+========+
    | KIND(1) | ACK(1) | CRC(4) |
    +=========+========+========+
*/

