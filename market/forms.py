from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('أسم المستخدم موجود بالفعل ')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError(' البريد الأكتروني موجود بالفعل')

    username = StringField(label='أسم المستخدم:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='البريد الألكتروني:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='كلمة المرور:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='تأكيد كلمة المرور:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='إنشاء حساب')


class LoginForm(FlaskForm):
    username = StringField(label='أسم المستخدم:', validators=[DataRequired()])
    password = PasswordField(label='كلمة المرور:', validators=[DataRequired()])
    submit = SubmitField(label='تسجيل الدخول')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='شراء العنصر')


class SellItemForm(FlaskForm):
    submit = SubmitField(label='بيع العنصر')
