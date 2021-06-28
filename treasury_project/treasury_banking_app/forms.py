# from django import forms
#
#
# class UserEditForm(forms.Form):
#     CREATE_PAYMENT = 'CR'
#     DELETE_PAYMENT = 'DP'
#     APPROVE_PAYMENT = 'AP'
#     PERMISSION_CHOICE = [
#         (CREATE_PAYMENT, 'Create Payment'),
#         (DELETE_PAYMENT, 'Delete Payment'),
#         (APPROVE_PAYMENT, 'Approve Payment'),
#     ]
#     name = forms.CharField(max_length=255)
#     surname = forms.CharField(max_length=255, blank=False)
#     internal_id = forms.CharField(max_length=7, blank=False)
#     permission_type = forms.CharField(max_length=2, choices=PERMISSION_CHOICE, default=CREATE_PAYMENT)
#     account = forms.MultipleChoiceField(queryset=Account)
#     is_administrator = models.BooleanField(default=False)
