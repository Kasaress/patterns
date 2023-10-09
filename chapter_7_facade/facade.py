from devices import (Amplifier, PopcornPopper, Projector, Screen,
                     StreamingPlayer, TheaterLights, Tuner)


class HomeTheaterFacade:
    amp = Amplifier()
    uner = Tuner()
    player = StreamingPlayer()
    projector = Projector()
    screen = Screen()
    lights = TheaterLights()
    popper = PopcornPopper()

    def watch_movie(self, movie: str) -> None:
        print(f'Начинаем просмотр {movie}.')
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_streaming_player(self.player)
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.player.on()
        self.player.play(movie)

    def end_movie(self) -> None:
        print('Завершаем просмотр фильма.')
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.player.stop()
        self.player.off()

    def listen_to_radio(self) -> None:
        pass

    def end_radio(self) -> None:
        pass
