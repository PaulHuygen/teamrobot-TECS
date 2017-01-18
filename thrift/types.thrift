namespace java de.dfki.tecs.examples.helloworld
namespace cpp de.dfki.tecs.examples.helloworld
namespace csharp de.dfki.tecs.examples.helloworld
namespace py de.dfki.tecs.examples.helloworld
namespace rb de.dfki.tecs.examples.helloworld


struct HelloWorldEvent {
	1:required string message = "HelloWorld";
}


service HWEService {
	string hello(1:string text);
}


