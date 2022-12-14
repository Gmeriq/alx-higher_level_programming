#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
listint_t *current, *new;

if (head == NULL)
return (NULL);
new = malloc(sizeof(listint_t));

if (new == NULL)
return (NULL);
new->n = number;
new->next = NULL;

if (*head == NULL)
{
*head = new;
return (new);
}
current = *head;
if (current->n > new->n)
{
new->next = current;
*head = new;
return (new);
}

while(current && current->next)
{
if (current->next->n < new->n)
current = current->next;
else
{
new->next = current->next;
current->next = new;
return (new);
}
current->next = new;
return (new);
}
}
