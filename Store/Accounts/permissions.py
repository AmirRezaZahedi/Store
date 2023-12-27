from rest_framework import permissions



class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        pk = view.kwargs.get('pk')
        if request.method == "POST":
            return True
        elif request.method == "GET":

            if(bool(request.user and request.user.is_authenticated)):
        
                if(request.user.access == 1):
                    return True
                if(pk):
                    pk=int(pk)
                    if(bool(request.user.customer.id == pk)):
                        return True

        elif request.method == "PUT" or request.method == "DELETE":
            pk=int(pk)
            if(bool(request.user and request.user.is_authenticated)):
                 return bool(request.user.access == 0 and request.user.customer.id == pk) 
        
        return False


class IsSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        pk = view.kwargs.get('pk')
        if request.method == "POST":
            return True
        elif request.method == "GET":

            if(bool(request.user and request.user.is_authenticated)):
                return bool(request.user.access == 0)

        elif request.method == "PUT" or request.method == "DELETE":
            pk=int(pk)
            if(bool(request.user and request.user.is_authenticated)):
                 return bool(request.user.access == 0 and request.user.seller.id == pk)
             
        return False