import os
import mmap
import struct

# A brief description of the MIDI specification:
#
# http://www.somascape.org/midi/tech/spec.html
#
# A brief description of the MIDI File specification:
#
# http://www.somascape.org/midi/tech/mfile.html
#
# A MIDI Binary Template:
#
# https://www.sweetscape.com/010editor/repository/files/MIDI.bt
#
# A description of Running Status:
#
# http://midi.teragonaudio.com/tech/midispec/run.htm

class NoteOnEvent():
    def __init__(self, deltaTime, channel, memoryMap):
        self.deltaTime = deltaTime
        self.channel = channel
        self.note = struct.unpack("B", memoryMap.read(1))[0]
        self.velocity = struct.unpack("B", memoryMap.read(1))[0]

class NoteOffEvent():
    def __init__(self, deltaTime, channel, memoryMap):
        self.deltaTime = deltaTime
        self.channel = channel
        self.note = struct.unpack("B", memoryMap.read(1))[0]
        self.velocity = struct.unpack("B", memoryMap.read(1))[0]

class NotePressureEvent():
    def __init__(self, deltaTime, channel, memoryMap):
        self.deltaTime = deltaTime
        self.channel = channel
        self.note = struct.unpack("B", memoryMap.read(1))[0]
        self.pressure = struct.unpack("B", memoryMap.read(1))[0]

class ControllerEvent():
    def __init__(self, deltaTime, channel, memoryMap):
        self.deltaTime = deltaTime
        self.channel = channel
        self.controller = struct.unpack("B", memoryMap.read(1))[0]
        self.value = struct.unpack("B", memoryMap.read(1))[0]

class ProgramEvent():
    def __init__(self, deltaTime, channel, memoryMap):
        self.deltaTime = deltaTime
        self.channel = channel
        self.note = struct.unpack("B", memoryMap.read(1))[0]
        self.velocity = struct.unpack("B", memoryMap.read(1))[0]

class ChannelPressureEvent():
    def __init__(self, deltaTime, channel, memoryMap):
        self.deltaTime = deltaTime
        self.channel = channel
        self.pressure = struct.unpack("B", memoryMap.read(1))[0]

class PitchBendEvent():
    def __init__(self, deltaTime, channel, memoryMap):
        self.deltaTime = deltaTime
        self.channel = channel
        self.lsb = struct.unpack("B", memoryMap.read(1))[0]
        self.msb = struct.unpack("B", memoryMap.read(1))[0]

class SequenceNumberEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.sequenceNumber = struct.unpack(">H", memoryMap.read(2))[0]

class TextEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.text = struct.unpack(f"{length}s", memoryMap.read(length))[0].decode("ascii")

class CopyrightEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.copyright = struct.unpack(f"{length}s", memoryMap.read(length))[0].decode("ascii")

class TrackNameEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.name = struct.unpack(f"{length}s", memoryMap.read(length))[0].decode("ascii")

class InstrumentNameEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.name = struct.unpack(f"{length}s", memoryMap.read(length))[0].decode("ascii")

class LyricEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.lyric = struct.unpack(f"{length}s", memoryMap.read(length))[0].decode("ascii")

class MarkerEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.marker = struct.unpack(f"{length}s", memoryMap.read(length))[0].decode("ascii")

class CuePointEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.cuePoint = struct.unpack(f"{length}s", memoryMap.read(length))[0].decode("ascii")

class ProgramNameEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.name = struct.unpack(f"{length}s", memoryMap.read(length))[0].decode("ascii")

class DeviceNameEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.name = struct.unpack(f"{length}s", memoryMap.read(length))[0].decode("ascii")

class MidiChannelPrefixEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.prefix = struct.unpack("B", memoryMap.read(1))[0]

class MidiPortEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.port = struct.unpack("B", memoryMap.read(1))[0]

class EndOfTrackEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime

class TempoEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.tempo = struct.unpack(">I", b'\x00' + memoryMap.read(3))[0]

class SmpteOffsetEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.hours = struct.unpack("B", memoryMap.read(1))[0]
        self.minutes = struct.unpack("B", memoryMap.read(1))[0]
        self.seconds = struct.unpack("B", memoryMap.read(1))[0]
        self.fps = struct.unpack("B", memoryMap.read(1))[0]
        self.fractionalFrames = struct.unpack("B", memoryMap.read(1))[0]

class TimeSignatureEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.numerator = struct.unpack("B", memoryMap.read(1))[0]
        self.denominator = struct.unpack("B", memoryMap.read(1))[0]
        self.clocksPerClick = struct.unpack("B", memoryMap.read(1))[0]
        self.thirtySecondPer24Clocks = struct.unpack("B", memoryMap.read(1))[0]

class KeySignatureEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.flatsSharps = struct.unpack("B", memoryMap.read(1))[0]
        self.majorMinor = struct.unpack("B", memoryMap.read(1))[0]

class SequencerEvent():
    def __init__(self, deltaTime, length, memoryMap):
        self.deltaTime = deltaTime
        self.data = struct.unpack(f"{length}s", memoryMap.read(length))[0]

metaEventByType = {
    0x00 : SequenceNumberEvent,
    0x01 : TextEvent,
    0x02 : CopyrightEvent,
    0x03 : TrackNameEvent,
    0x04 : InstrumentNameEvent,
    0x05 : LyricEvent,
    0x06 : MarkerEvent,
    0x07 : CuePointEvent,
    0x08 : ProgramNameEvent,
    0x09 : DeviceNameEvent,
    0x20 : MidiChannelPrefixEvent,
    0x21 : MidiPortEvent,
    0x2F : EndOfTrackEvent,
    0x51 : TempoEvent,
    0x54 : SmpteOffsetEvent,
    0x58 : TimeSignatureEvent,
    0x59 : KeySignatureEvent,
    0x7F : SequencerEvent,
}

channelEventByStatus = {
    0x80 : NoteOffEvent,
    0x90 : NoteOnEvent,
    0xA0 : NotePressureEvent,
    0xB0 : ControllerEvent,
    0xC0 : ProgramEvent,
    0xD0 : ChannelPressureEvent,
    0xE0 : PitchBendEvent,
}

def unpackVLQ(memoryMap):
    total = 0
    while True:
        char = struct.unpack("B", memoryMap.read(1))[0]
        total = (total << 7) + (char & 0x7F)
        if not char & 0x80: break
    return total

class MidiFile():
    def __init__(self, filePath):
        self.tracks = []

        with open(filePath, "rb") as f:
            memoryMap = mmap.mmap(f.fileno(), 0, prot = mmap.PROT_READ)
            self.parseHeader(memoryMap)
            self.parseTracks(memoryMap)
            memoryMap.close()

    def parseHeader(self, memoryMap):
        identifier = memoryMap.read(4).decode('ascii')
        chunkLength = struct.unpack(">I", memoryMap.read(4))[0]
        self.format = struct.unpack(">H", memoryMap.read(2))[0]
        self.tracksCount = struct.unpack(">H", memoryMap.read(2))[0]
        self.ppqn = struct.unpack(">H", memoryMap.read(2))[0]

    def parseTracks(self, memoryMap):
        for i in range(self.tracksCount):
            self.tracks.append(MidiTrack(memoryMap))

class MidiTrack():
    def __init__(self, memoryMap):
        self.events = []
        self.runningStatus = 0

        self.parseHeader(memoryMap)
        self.parseEvents(memoryMap)

    def parseHeader(self, memoryMap):
        identifier = memoryMap.read(4).decode('ascii')
        self.chunkLength = struct.unpack(">I", memoryMap.read(4))[0]

    def parseEvents(self, memoryMap):
        while True:
            event = self.parseEvent(memoryMap)
            self.events.append(event)
            if isinstance(event, EndOfTrackEvent): break

    def parseEvent(self, memoryMap):
        deltaTime = unpackVLQ(memoryMap)
        status = struct.unpack("B", memoryMap.read(1))[0]
        
        if status & 0x80: self.runningStatus = status
        else: memoryMap.seek(-1, os.SEEK_CUR)

        if self.runningStatus == 0xFF:
            return self.parseMetaEvent(deltaTime, memoryMap)
        elif self.runningStatus >= 0x80:
            return self.parseChannelEvent(deltaTime, self.runningStatus, memoryMap)
        elif self.runningStatus == 0xF0 or self.runningStatus == 0xF7:
            return self.parseSysExEvent(deltaTime, memoryMap)

    def parseChannelEvent(self, deltaTime, status, memoryMap):
        channel = status & 0xF
        eventClass = channelEventByStatus[status & 0xF0]
        event = eventClass(deltaTime, channel, memoryMap)
        return event

    def parseMetaEvent(self, deltaTime, memoryMap):
        eventType = struct.unpack("B", memoryMap.read(1))[0]
        length = unpackVLQ(memoryMap)

        eventClass = metaEventByType[eventType]
        event = eventClass(deltaTime, length, memoryMap)
        return event

    def parseSysExEvent(self, deltaTime, memoryMap):
        pass

