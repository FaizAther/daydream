#include <stdio.h>
#include <stdlib.h>
#include <math.h>

unsigned long long int
fib_r(unsigned long long int n)
{
    if (n == 0)
        return 0;
    else if (n == 1)
        return 1;
    else
        return fib_r(n-1) + fib_r(n-2);
}

typedef struct _list *List;

typedef struct _list {
	struct _node 	*head;
	struct _node	*tail;
	unsigned long long int		size;
} list;

typedef struct _node *Node;

typedef struct _node {
	unsigned long long int		data;
	struct _node 	*next;
	struct _node	*prev;
} node;

void
append(List list, unsigned long long int number)
{
	Node node = (Node)malloc(sizeof(*node));
	node->data = number;
	node->next = node->prev = NULL;
	if (list->size == 0) {
		list->head = list->tail = node;
	} else {
		node->prev = list->tail;
		list->tail = node;
	}
	list->size += 1;
}

unsigned long long int
fib_r_o(unsigned long long int n)
{
    List list = (List)malloc(sizeof(*list));
    append(list, 0);
    append(list, 1);
    unsigned long long int i = 2;
    while(i != n+1) {
	append(list, list->tail->data + list->tail->prev->data);
	//prunsigned long long int(list[i])
	i += 1;
    }
    return list->tail->data;
}

unsigned long long int
fib_c(unsigned long long int n)
{
    return ((1.0/ (sqrt(5.0) ) * (pow(((1.0 / 2.0) + sqrt(5.0 / 4.0)), n) - pow(((1.0 / 2.0) - sqrt(5.0 / 4.0)), n))));
}

int
main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: fib <n>");
    } else {
        printf("constant\t\ttime fib n=%s, res=%llu\n", argv[1], (unsigned long long int)(fib_c((unsigned long long int)atoi(argv[1]))));
        printf("optimized\t\ttime fib n=%s, res=%llu\n", argv[1], (unsigned long long int)(fib_r_o((unsigned long long int)atoi(argv[1]))));
    }
}
