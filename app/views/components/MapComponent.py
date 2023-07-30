from app.views.components.Component import Component
import customtkinter as ctk
import tkintermapview as map


class MapComponent(Component):

    def __init__(self, container, last_frame=None):
        super().__init__(container, last_frame)
        # label = ctk.CTkLabel(self, text="Mapa", font=("Roboto", 25))
        # label.pack(padx=10, pady=10, anchor=ctk.CENTER)

        self.loadBody()

        self.main()

    def loadBody(self):
        map_widget = map.TkinterMapView(self, width=1000, height=700, corner_radius=0)
        map_widget.pack(fill="both", expand=True)

        map_widget.set_position(-24.78897, -65.4104, marker=False)

        # set a position marker (also with a custom color and command on click)
        marker_2 = map_widget.set_marker(52.516268, 13.377695, text="Brandenburger Tor", command=lambda marker: self.marker_click(marker))
        marker_3 = map_widget.set_marker(52.55, 13.4, text="52.55, 13.4")

        # path_1 = map_widget.set_path([marker_2.position, marker_3.position, (52.568, 13.4), (52.569, 13.35)])

    def marker_click(self, marker):
        print(f"marker clicked - text: {marker.text}  position: {marker.position}")