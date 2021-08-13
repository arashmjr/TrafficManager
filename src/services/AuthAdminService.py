from src.repository.AdminUserRepository import AdminUserRepository
from src.services.Manager.AuthorizationManager import make_token_for_admin
from src.domain.models.AdminUserDomainModel import AdminUserDomainModel
import re
import datetime
import hashlib


class AuthAdminService:
    repository_admin: AdminUserRepository

    regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'

    def __init__(self, repository_admin: AdminUserRepository):
        self.repository_admin = repository_admin

    def sign_up_admin(self, json) -> str:

        if re.search(self.regex, json['email']):
            record = self.repository_admin.find_record_by_email_signup(json['email'])
            if record.count() == 0:
                if json['password'] == json['confirm_password']:

                    hashed_password = hashlib.md5(json['password'].encode('utf-8')).hexdigest()
                    creation_date = datetime.datetime.now()
                    model = AdminUserDomainModel(
                                                    json['name'],
                                                    json['email'],
                                                    hashed_password,
                                                    creation_date
                                                )
                    print(model.creation_date)
                    self.repository_admin.insert(model)

                    item = self.repository_admin.find_record_by_email(json['email'])
                    admin_id = item.admin_id

                    # create token for user
                    token = make_token_for_admin(admin_id)
                    print(token)
                    # token_utf = token.decode('utf-8')
                    return token

                raise Exception("Sorry, password & confirm-pass is not equal")

            raise Exception("This email isn't available. Please try another.")

        raise ValueError

    def login_admin(self, json) -> str:

        if re.search(self.regex, json['email']):
            record = self.repository_admin.find_record_by_email(json['email'])

            if record is not None:
                hashed_password = hashlib.md5(json['password'].encode('utf-8')).hexdigest()
                if record.password == hashed_password:
                    admin_id = record.admin_id
                    token = make_token_for_admin(admin_id)
                    # token_utf = token.decode('utf-8')
                    return token

                raise Exception("Sorry, your password was incorrect. Please double-check your password.")

            raise Exception("The email you entered doesn't belong to an account.Please check your email and try again.")

        raise ValueError
