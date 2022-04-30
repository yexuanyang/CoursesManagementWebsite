from wtforms import IntegerField, TextAreaField, SubmitField, StringField, validators, TimeField,ValidationError,DateField
from flask_wtf import FlaskForm

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

