import recorder, replayer

rec = recorder.InputRecorder()
rec.start()

input("press enter to replay")

rep = replayer.InputReplayer(rec.events)
rep.start()


