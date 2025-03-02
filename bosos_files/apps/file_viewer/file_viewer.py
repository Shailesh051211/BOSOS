# pylint: disable=all

from __future__ import annotations

from typing import override

import babase
import bauiv1 as bui
import bascenev1 as bs

from bauiv1lib.qrcode import QRCodeWindow
from bosos_files.app_window import AppWindow

import os
import functools

# export app FileViewer
class FileViewerScreen(AppWindow):

    def __init__(
        self,
        width: float = 800.0,
        height: float = 550.0,
        transition: str | None = 'in_right',
        origin_widget: bui.Widget | None = None,
    ):
        # pylint: disable=too-many-statements
        app = bui.app
        assert app.classic is not None

        super().__init__(
            width=width,
            height=height,
            transition=transition,
            origin_widget=origin_widget,
        )

        self._audio_button: bui.Widget | None = None
        self._texture_button: bui.Widget | None = None

        self._build_ui()

    @override
    def get_main_window_state(self) -> bui.MainWindowState:
        # Support recreating our window for back/refresh purposes.
        cls = type(self)
        return bui.BasicMainWindowState(
            create_call=lambda transition, origin_widget: cls(
                transition=transition, origin_widget=origin_widget
            )
        )

    @override
    def on_main_window_close(self) -> None:
        pass

    def _build_ui(self) -> None:
        self._audio_button = bui.buttonwidget(
            parent=self._root_widget,
            position=(self._width/2 - 180, self._height/2),
            size=(360, 120),
            label='Audio',
            text_scale=1.3,
        )
        self._texture_button = bui.buttonwidget(
            parent=self._root_widget,
            position=(self._width/2 - 180, self._height/2 - 130),
            size=(360, 120),
            label='Textures',
            text_scale=1.3,
            on_activate_call=self._open_textures_window
        )

    def _open_textures_window(self):
        if not self.main_window_has_control():
            return