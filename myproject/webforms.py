from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, EmailField, ValidationError
from wtforms.validators import DataRequired, Email, Length, EqualTo
from myproject.models import User

# Create a Register Form
class RegistrationForm(FlaskForm):
    username = StringField("使用者名稱",validators=[DataRequired(),Length(4,25)])
    email = EmailField("電子郵件", validators=[DataRequired(),Length(6,35)])
    password = PasswordField("密碼", validators=[DataRequired(),Length(6,10),EqualTo('confirm_password', message='密碼需要吻合')])
    confirm_password = PasswordField("確認密碼",validators=[DataRequired()])
    submit = SubmitField("註冊")

    def check_email(self, field):
        """檢查Email"""
        if  User.query.filter_by(email=field.data).first():
            raise ValidationError('電子郵件已經被註冊過了')

    def check_username(self, field):
        """檢查username"""
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('使用者名稱已經存在')


# Create Login Form
class LoginForm(FlaskForm):
	# email = EmailField("電子郵件", validators=[DataRequired(), Length(6,35)])
    username = StringField("使用者名稱",validators=[DataRequired(),Length(4,25)])
    password = PasswordField("密碼", validators=[DataRequired(),Length(6,10)])
    remember_me = BooleanField("保持登入")
    submit = SubmitField("登入")
