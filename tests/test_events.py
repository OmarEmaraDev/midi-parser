import struct
from io import BytesIO
from midiparser.events import *

class TestChannelEvents:
    def test_NoteOnEvent(self):
        deltaTime = 100
        channel = 2
        note = 45
        velocity = 64

        referenceEvent = NoteOnEvent(deltaTime, channel, note, velocity)

        memoryMap = BytesIO(struct.pack("BB", note, velocity))
        parsedEvent = NoteOnEvent.fromMemoryMap(deltaTime, channel, memoryMap)

        assert referenceEvent == parsedEvent

    def test_NoteOffEvent(self):
        deltaTime = 100
        channel = 2
        note = 45
        velocity = 64

        referenceEvent = NoteOffEvent(deltaTime, channel, note, velocity)

        memoryMap = BytesIO(struct.pack("BB", note, velocity))
        parsedEvent = NoteOffEvent.fromMemoryMap(deltaTime, channel, memoryMap)

        assert referenceEvent == parsedEvent

    def test_NotePressureEvent(self):
        deltaTime = 100
        channel = 2
        note = 45
        pressure = 64

        referenceEvent = NotePressureEvent(deltaTime, channel, note, pressure)

        memoryMap = BytesIO(struct.pack("BB", note, pressure))
        parsedEvent = NotePressureEvent.fromMemoryMap(deltaTime, channel, memoryMap)

        assert referenceEvent == parsedEvent

    def test_ControllerEvent(self):
        deltaTime = 100
        channel = 2
        controller = 45
        value = 64

        referenceEvent = ControllerEvent(deltaTime, channel, controller, value)

        memoryMap = BytesIO(struct.pack("BB", controller, value))
        parsedEvent = ControllerEvent.fromMemoryMap(deltaTime, channel, memoryMap)

        assert referenceEvent == parsedEvent

    def test_ProgramEvent(self):
        deltaTime = 100
        channel = 2
        program = 45

        referenceEvent = ProgramEvent(deltaTime, channel, program)

        memoryMap = BytesIO(struct.pack("B", program))
        parsedEvent = ProgramEvent.fromMemoryMap(deltaTime, channel, memoryMap)

        assert referenceEvent == parsedEvent

    def test_ChannelPressureEvent(self):
        deltaTime = 100
        channel = 2
        pressure = 45

        referenceEvent = ChannelPressureEvent(deltaTime, channel, pressure)

        memoryMap = BytesIO(struct.pack("B", pressure))
        parsedEvent = ChannelPressureEvent.fromMemoryMap(deltaTime, channel, memoryMap)

        assert referenceEvent == parsedEvent

    def test_PitchBendEvent(self):
        deltaTime = 100
        channel = 2
        lsb = 45
        msb = 64

        referenceEvent = PitchBendEvent(deltaTime, channel, lsb, msb)

        memoryMap = BytesIO(struct.pack("BB", lsb, msb))
        parsedEvent = PitchBendEvent.fromMemoryMap(deltaTime, channel, memoryMap)

        assert referenceEvent == parsedEvent

class TestMetaEvents:
    def test_SequenceNumberEvent(self):
        deltaTime = 100
        sequenceNumber = 64

        referenceEvent = SequenceNumberEvent(deltaTime, sequenceNumber)

        memoryMap = BytesIO(struct.pack(">H", sequenceNumber))
        parsedEvent = SequenceNumberEvent.fromMemoryMap(deltaTime, 0, memoryMap)

        assert referenceEvent == parsedEvent

    def test_TextEvent(self):
        deltaTime = 100
        text = "A test text."
        length = len(text)

        referenceEvent = TextEvent(deltaTime, text)

        memoryMap = BytesIO(struct.pack(f"{length}s", text.encode("ascii")))
        parsedEvent = TextEvent.fromMemoryMap(deltaTime, length, memoryMap)

        assert referenceEvent == parsedEvent

    def test_CopyrightEvent(self):
        deltaTime = 100
        copyright = "A test copyright."
        length = len(copyright)

        referenceEvent = CopyrightEvent(deltaTime, copyright)

        memoryMap = BytesIO(struct.pack(f"{length}s", copyright.encode("ascii")))
        parsedEvent = CopyrightEvent.fromMemoryMap(deltaTime, length, memoryMap)

        assert referenceEvent == parsedEvent

    def test_TrackNameEvent(self):
        deltaTime = 100
        name = "A test name."
        length = len(name)

        referenceEvent = TrackNameEvent(deltaTime, name)

        memoryMap = BytesIO(struct.pack(f"{length}s", name.encode("ascii")))
        parsedEvent = TrackNameEvent.fromMemoryMap(deltaTime, length, memoryMap)

        assert referenceEvent == parsedEvent

    def test_InstrumentNameEvent(self):
        deltaTime = 100
        name = "A test name."
        length = len(name)

        referenceEvent = InstrumentNameEvent(deltaTime, name)

        memoryMap = BytesIO(struct.pack(f"{length}s", name.encode("ascii")))
        parsedEvent = InstrumentNameEvent.fromMemoryMap(deltaTime, length, memoryMap)

        assert referenceEvent == parsedEvent

    def test_LyricEvent(self):
        deltaTime = 100
        lyric = "A test lyric."
        length = len(lyric)

        referenceEvent = LyricEvent(deltaTime, lyric)

        memoryMap = BytesIO(struct.pack(f"{length}s", lyric.encode("ascii")))
        parsedEvent = LyricEvent.fromMemoryMap(deltaTime, length, memoryMap)

        assert referenceEvent == parsedEvent

    def test_MarkerEvent(self):
        deltaTime = 100
        marker = "A test marker."
        length = len(marker)

        referenceEvent = MarkerEvent(deltaTime, marker)

        memoryMap = BytesIO(struct.pack(f"{length}s", marker.encode("ascii")))
        parsedEvent = MarkerEvent.fromMemoryMap(deltaTime, length, memoryMap)

        assert referenceEvent == parsedEvent

    def test_CuePointEvent(self):
        deltaTime = 100
        cuePoint = "A test cue point."
        length = len(cuePoint)

        referenceEvent = CuePointEvent(deltaTime, cuePoint)

        memoryMap = BytesIO(struct.pack(f"{length}s", cuePoint.encode("ascii")))
        parsedEvent = CuePointEvent.fromMemoryMap(deltaTime, length, memoryMap)

        assert referenceEvent == parsedEvent

    def test_ProgramNameEvent(self):
        deltaTime = 100
        name = "A test name."
        length = len(name)

        referenceEvent = ProgramNameEvent(deltaTime, name)

        memoryMap = BytesIO(struct.pack(f"{length}s", name.encode("ascii")))
        parsedEvent = ProgramNameEvent.fromMemoryMap(deltaTime, length, memoryMap)

        assert referenceEvent == parsedEvent

    def test_DeviceNameEvent(self):
        deltaTime = 100
        name = "A test name."
        length = len(name)

        referenceEvent = DeviceNameEvent(deltaTime, name)

        memoryMap = BytesIO(struct.pack(f"{length}s", name.encode("ascii")))
        parsedEvent = DeviceNameEvent.fromMemoryMap(deltaTime, length, memoryMap)

        assert referenceEvent == parsedEvent

    def test_MidiChannelPrefixEvent(self):
        deltaTime = 100
        prefix = 64

        referenceEvent = MidiChannelPrefixEvent(deltaTime, prefix)

        memoryMap = BytesIO(struct.pack("B", prefix))
        parsedEvent = MidiChannelPrefixEvent.fromMemoryMap(deltaTime, 0, memoryMap)

        assert referenceEvent == parsedEvent

    def test_MidiPortEvent(self):
        deltaTime = 100
        port = 64

        referenceEvent = MidiPortEvent(deltaTime, port)

        memoryMap = BytesIO(struct.pack("B", port))
        parsedEvent = MidiPortEvent.fromMemoryMap(deltaTime, 0, memoryMap)

        assert referenceEvent == parsedEvent

    def test_EndOfTrackEvent(self):
        deltaTime = 100

        referenceEvent = EndOfTrackEvent(deltaTime)

        memoryMap = BytesIO()
        parsedEvent = EndOfTrackEvent.fromMemoryMap(deltaTime, 0, memoryMap)

        assert referenceEvent == parsedEvent

    def test_TempoEvent(self):
        deltaTime = 100
        tempo = 500000

        referenceEvent = TempoEvent(deltaTime, tempo)

        memoryMap = BytesIO(struct.pack(">I", tempo)[1:])
        parsedEvent = TempoEvent.fromMemoryMap(deltaTime, 0, memoryMap)

        assert referenceEvent == parsedEvent

    def test_SmpteOffsetEvent(self):
        deltaTime = 100
        hours = 1
        minutes = 12
        seconds = 50
        fps = 24
        fractionalFrames = 2

        referenceEvent = SmpteOffsetEvent(deltaTime, hours, minutes, seconds, fps, fractionalFrames)

        memoryMap = BytesIO(struct.pack("BBBBB", hours, minutes, seconds, fps, fractionalFrames))
        parsedEvent = SmpteOffsetEvent.fromMemoryMap(deltaTime, 0, memoryMap)

        assert referenceEvent == parsedEvent

    def test_TimeSignatureEvent(self):
        deltaTime = 100
        numerator = 1
        denominator = 12
        clocksPerClick = 50
        thirtySecondPer24Clocks = 24

        referenceEvent = TimeSignatureEvent(deltaTime, numerator, denominator, clocksPerClick, thirtySecondPer24Clocks)

        memoryMap = BytesIO(struct.pack("BBBB", numerator, denominator, clocksPerClick, thirtySecondPer24Clocks))
        parsedEvent = TimeSignatureEvent.fromMemoryMap(deltaTime, 0, memoryMap)

        assert referenceEvent == parsedEvent

    def test_KeySignatureEvent(self):
        deltaTime = 100
        flatsSharps = 1
        majorMinor = 12

        referenceEvent = KeySignatureEvent(deltaTime, flatsSharps, majorMinor)

        memoryMap = BytesIO(struct.pack("BB", flatsSharps, majorMinor))
        parsedEvent = KeySignatureEvent.fromMemoryMap(deltaTime, 0, memoryMap)

        assert referenceEvent == parsedEvent

    def test_SequencerEvent(self):
        deltaTime = 100
        data = b"\x00\x32\xA5"
        length = len(data)

        referenceEvent = SequencerEvent(deltaTime, data)

        memoryMap = BytesIO(data)
        parsedEvent = SequencerEvent.fromMemoryMap(deltaTime, length, memoryMap)

        assert referenceEvent == parsedEvent

class TestSysExEvents:
    def test_SysExEvent(self):
        deltaTime = 100
        data = b"\x00\x32\xA5"
        length = len(data)

        referenceEvent = SysExEvent(deltaTime, data)

        memoryMap = BytesIO(data)
        parsedEvent = SysExEvent.fromMemoryMap(deltaTime, length, memoryMap)

        assert referenceEvent == parsedEvent

    def test_EscapeSequenceEvent(self):
        deltaTime = 100
        data = b"\x00\x32\xA5"
        length = len(data)

        referenceEvent = EscapeSequenceEvent(deltaTime, data)

        memoryMap = BytesIO(data)
        parsedEvent = EscapeSequenceEvent.fromMemoryMap(deltaTime, length, memoryMap)

        assert referenceEvent == parsedEvent

