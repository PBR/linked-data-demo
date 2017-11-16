# Installation and setup

This is the Linked Data Demonstrator ran by WUR. It is currently running at [https://www.plantbreeding.wur.nl/ld-demonstrator/](https://www.plantbreeding.wur.nl/ld-demonstrator/).

Instructions for its setup can be found below.

This project is based on an earlier version of [DTL's linked data demonstrator](https://github.com/DTL-FAIRData/linked-data-demo).

## Set up Blazegraph

* Get the [executable jar](https://wiki.blazegraph.com/wiki/index.php/NanoSparqlServer#Downloading_the_Executable_Jar).
* Run the server:  
  `java -server -Xmx4g -jar path/to/blazegraph.jar`  
  <!--`java -server -Xmx4g -jar C:\Users\papou001\My_portable_apps\Blazegraph\blazegraph.jar`  -->
  
* The Blazegraph GUI should now be live at [`http://localhost:9999`](http://localhost:9999)

* Create a namespace for your project at [`http://localhost:9999/blazegraph/#namespaces`](http://localhost:9999/blazegraph/#namespaces). 

![Creating a namespace](images/namespace.png "Creating the namespace")
For this example, the namespace will be `ldd-demo`. After creating it, make sure to also `Use` the namespace.

* Go to the [Update tab](http://localhost:9999/blazegraph/#update) to load your data (triples). You can click on `Browse` to manually select your files in the filesystem, or provide the commands in the interface with the absolute paths for the files (e.g. `load <file:///tmp/blazegraph/data.n3>`), as seen on the screenshot. Make sure that the correct namespace is used.

![Importing data](images/data_import.png "Importing the data (ttl files)")

* Verify that this particular namespace can be queried. You can do this through the `Query tab`.  
Alternatively, you can submit a request directly.
E.g. to query with `select distinct ?p where {?s ?p ?o} limit 10 `, navigate to
[`http://localhost:9999/blazegraph/namespace/ldd-demo/sparql?format=json&query=select distinct ?p where {?s ?p ?o} limit 10`](http://localhost:9999/blazegraph/namespace/ldd-demo/sparql?format=json&query=select%20distinct%20%3Fp%20where%20%7B%3Fs%20%3Fp%20%3Fo%7D%20limit%2010)  
In this case, the base URL for querying your namespace is `http://localhost:9999/blazegraph/namespace/ldd-demo/sparql`.


## Set up the redirection layer

Clone the [linked-data-demo_redirect project](https://github.com/PBR/linked-data-demo_redirect) and follow the instructions there.




















