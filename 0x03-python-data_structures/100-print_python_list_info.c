#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints python list info
 *
 * @p: PyObject
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	long int size, x;
	PyListObject *listob;
	PyObject *unit;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	listob = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", listob->allocated);

	for (x = 0; x < size; x++)
	{
		unit = PyList_GetItem(p, x);
		printf("Element %ld: %s\n", x, Py_TYPE(unit)->tp_name);
	}
}
