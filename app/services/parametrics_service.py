class ParametricService:

    def get_links(self):
        return [
            ('Actividades', 'tour', 'tour-icon', False),
            ('Explorar Destinos', 'map', 'map-icon', False),
            ('Planificar', 'plain', 'tour-icon', False),
            ('Reseñas', 'review', 'review-icon', False),
            ('Destinos', 'destiny', 'destiny-icon', True),
            ('Administracion', 'administration', 'admin-icon', True),
            ('Usuarios', 'users', 'users-icon', True)
        ]

    def get_center_map(self):
        return (-24.788919397299342, -65.410276474954)


parametric_service = ParametricService()
