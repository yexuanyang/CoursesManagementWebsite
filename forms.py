from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, validators, TimeField, DateField, SelectMultipleField


class OutCourseForms(FlaskForm):
    activity_name = StringField("活动名称", validators=[validators.DataRequired("请输入活动名称"),
                                                    validators.Length(-1, 20, None)])
    activity_time = DateField("活动时间", validators=[validators.DataRequired("请输入活动时间")])
    begin_time = TimeField("开始时间", validators=[validators.DataRequired("请输入开始时间")])
    end_time = TimeField("结束时间", validators=[validators.DataRequired("请输入开始时间")])
    persons_num = IntegerField("活动人数", validators=[validators.DataRequired("请输入活动人数"),
                                                   validators.NumberRange(1, 50, "活动人数最多为50人,请修改活动人数")])
    location = StringField("活动地点", validators=[validators.DataRequired("请输入活动地点")])
    submit = SubmitField("确定")


class InCourseForms(FlaskForm):
    cause_name = StringField("课程名称", validators=[validators.DataRequired("请输入课程名称"), validators.Length(-1, 20, None)])
    teacher = StringField("任课老师", validators=[validators.DataRequired("请输入教师名称"), validators.Length(-1, 10, None)])
    time = SelectMultipleField("上课时间", validators=[validators.DataRequired("请选择上课时间")],
                               choices={"课时": ['1，2节课', "3，4节课", "5，6节课", "7，8节课", "9，10节课",
                                               "11，12节课", "13，14节课", "15，16节课"]})
    day = SelectMultipleField(choices={"星期": ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六',
                                              '星期天']})
    location = StringField("上课地点", validators=[validators.DataRequired("请输入上课地点"), validators.Length(-1, 20, None)])
    qq = StringField("qq群", validators=[validators.DataRequired("请输入联系方式"), validators.Length(8, 20, None)])
    exam_time = DateField("考试时间", validators=[validators.DataRequired("请输入考试时间")])
    submit = SubmitField("确定")
