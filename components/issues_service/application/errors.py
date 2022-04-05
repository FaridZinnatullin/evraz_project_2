from classic.app.errors import AppError


class NoPermission(AppError):
    msg_template = "You have no permissions to perform this action"
    code = 'issues.no_permissions'


class issueAlreadyExist(AppError):
    msg_template = "This login is already occupied"
    code = 'issues.issue_already_exist'


class UncorrectedParams(AppError):
    msg_template = "You give me very bad params... I have no data for you"
    code = 'issues.bad_params'


class Bannedissue(AppError):
    msg_template = "This issue was banned in this chat"
    code = 'issues.banned_issue'


class UncorrectedLoginPassword(AppError):
    msg_template = "Incorrect issuename or password"
    code = 'issues.authorization'
