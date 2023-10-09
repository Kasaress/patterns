class Tuner:
    def on(self) -> None:
        print('Tuner on')

    def off(self) -> None:
        print('Tuner off')

    def set_am(self) -> None:
        print('Tuner set_am')

    def set_fm(self) -> None:
        print('Tuner set_fm')

    def set_frequency(self) -> None:
        print('Tuner set_frequency')

    def __repr__(self) -> str:
        return 'Tuner'


class Screen:
    def up(self) -> None:
        print('Screen up')

    def down(self) -> None:
        print('Screen down')

    def __repr__(self) -> str:
        return 'Screen'


class PopcornPopper:
    def on(self) -> None:
        print('PopcornPopper on')

    def off(self) -> None:
        print('PopcornPopper off')

    def pop(self) -> None:
        print('PopcornPopper pop')

    def __repr__(self) -> str:
        return 'ScrPopcornPoppereen'


class TheaterLights:
    def on(self) -> None:
        print('TheaterLights on')

    def off(self) -> None:
        print('TheaterLights off')

    def dim(self, value: int) -> None:
        print(f'TheaterLights dim {value}')

    def __repr__(self) -> str:
        return 'TheaterLights'


class Projector:
    def on(self) -> None:
        print('Projector on')

    def off(self) -> None:
        print('Projector off')

    def tv_mode(self) -> None:
        print('Projector tv_mode')

    def wide_screen_mode(self) -> None:
        print('Projector wide_screen_mode')

    def __repr__(self) -> str:
        return 'Projector'


class StreamingPlayer:
    def on(self) -> None:
        print('StreamingPlayer on')

    def off(self) -> None:
        print('StreamingPlayer off')

    def pause(self) -> None:
        print('StreamingPlayer pause')

    def play(self, movie: str) -> None:
        print(f'StreamingPlayer play {movie}')

    def set_surround_audio(self) -> None:
        print('StreamingPlayer set_surround_audio')

    def set_two_channel_audio(self) -> None:
        print('StreamingPlayer set_two_channel_audio')

    def stop(self) -> None:
        print('StreamingPlayer stop')

    def __repr__(self) -> str:
        return 'StreamingPlayer'


class Amplifier:
    def on(self) -> None:
        print('Amplifier on')

    def off(self) -> None:
        print('Amplifier off')

    def set_streaming_player(self, player: StreamingPlayer) -> None:
        print(f'Amplifier set_streaming_player {player}')

    def set_stereo_sound(self) -> None:
        print('Amplifier set_stereo_sound')

    def set_surround_sound(self) -> None:
        print('Amplifier set_surround_sound')

    def set_tuner(self) -> None:
        print('Amplifier set_tuner')

    def set_volume(self, value: int) -> None:
        print(f'Amplifier set_volume {value}')

    def __repr__(self) -> str:
        return 'StreamAmplifieringPlayer'
