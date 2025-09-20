package main

import (
	"C"
	"runtime"

	"github.com/ltcmweb/mwebd"
)

//export start
func start(chain, dataDir *C.char) C.int {
	args := &mwebd.ServerArgs{
		Chain:   C.GoString(chain),
		DataDir: C.GoString(dataDir),
	}
	server, err := mwebd.NewServer2(args)
	if err != nil {
		return 0
	}
	if runtime.GOOS != "windows" {
		if server.StartUnix(args.DataDir+"/mwebd.sock") == nil {
			return 1
		}
	} else if port, err := server.Start(0); err == nil {
		return C.int(port)
	}
	return 0
}

func main() {}
