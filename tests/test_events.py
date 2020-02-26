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

