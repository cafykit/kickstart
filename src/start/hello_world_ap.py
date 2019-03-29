from logger.cafylog import CafyLog
log=CafyLog("HelloWorld")

class TestHelloWorld:
    def test_hello_world(self):
        log.info("Hello World")

    def test_print_table(self):
        n = 5
        for i in range(1,11):
            log.info("{i}x{n}={result}".format(i=i,n=n,result=i*n))	
