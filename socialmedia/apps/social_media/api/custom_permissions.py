from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permissão personalizada para permitir apenas aos proprietários de um objeto editá-lo.
    """

    def has_object_permission(self, request, view, obj):
        # As solicitações de leitura são permitidas para qualquer solicitação,
        # então sempre permitiremos GET, HEAD ou OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Apenas o proprietário do snippet tem permissão para atualizar ou excluir.
        return obj.author == request.user
