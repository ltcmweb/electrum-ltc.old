package main

import (
	"C"

	"github.com/ltcmweb/mwebd"
)

//export Start
func Start(chain, dataDir *C.char) C.int {
	args := &mwebd.ServerArgs{
		Chain:   C.GoString(chain),
		DataDir: C.GoString(dataDir),
	}
	server, err := mwebd.NewServer2(args)
	if err != nil {
		return 0
	}
	if err = server.StartUnix(args.DataDir + "/mwebd.sock"); err != nil {
		return 0
	}
	return 1
}

func main() {}
