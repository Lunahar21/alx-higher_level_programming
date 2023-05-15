#include "listobject.h"
#include "object.h"
void print_python_list_info(PyObject *p)
{
	int i, l;

	l = PyList_Size(p)
	for (i = 0; i < l; i++)
	       print("[*] Size  of the Python List = %d", 1);	
}
