def get_permission(privilage):
    if privilage == 1:
        return "1111"
    elif privilage == 2:
        return "1110"
    elif privilage == 3:
        return "0100"

def get_notification_list(apiCol, userCol, agg):
    request_list = []
    user_list = []

    if agg:
        for user in userCol:
            temp_count = 0
            for api in apiCol:
                if str(api["user_request"]) == str(user.id):
                    temp_count += 1
            
            if temp_count != 0:
                temp_dict = {"user":user.username,"request_count":temp_count}
                request_list.append(temp_dict)

        return request_list
    else:
        for user in userCol:
            temp_count = 0
            for api in apiCol:
                if str(api.user_request.id) == str(user.id):
                    temp_count += 1
            
            if temp_count != 0:
                temp_dict = {"user":user.username,"request_count":temp_count}
                request_list.append(temp_dict)

        return request_list