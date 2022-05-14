#include <stdio.h>
#include <stdlib.h>

typedef enum { //type
    ATOM,
    LIST
} type;

typedef char atom;
struct _listnode;

typedef struct { //element
    type type; //atom or list
    union {
        atom a;
        struct _listnode* listptr;
    };
} element;

typedef struct _listnode {
    type type;
    element el;
    struct _listnode* next;
} *list;

const element NIL = { .type = LIST, .listptr = NULL };

//fct declerations for Q5,Q6, Q7
element aasel(atom a);
element lasel(list l);
element car(element e);
list cdr(element e);
list cddr(element e);
list cons(element e, list l);
list append(list l1, list l2);
void freelist(list l);
void printlist(element e);
void insert(list* root, element item);


int main() {

    list L = (list)malloc(sizeof(struct _listnode));
    L->el.type = ATOM;
    L->el.a = 'a';

    list L2 = (list)malloc(sizeof(struct _listnode));
    L2->el.type = LIST;
    L->next = L2;

    list LB = (list)malloc(sizeof(struct _listnode));
    L2->el.listptr = LB;
    LB->el.type = ATOM;
    LB->el.a = 'b';

    list LC = (list)malloc(sizeof(struct _listnode));
    LC->el.type = ATOM;
    LC->el.a = 'c';
    LC->next = NULL;

    list LD = (list)malloc(sizeof(struct _listnode));
    LD->el.type = ATOM;
    LD->el.a = 'd';

    list LE = (list)malloc(sizeof(struct _listnode));
    LE->el.type = ATOM;
    LE->el.a = 'e';
    LE->next = NULL;

    LB->next = LC;
    L2->next = LD;
    LD->next = LE;
 

    list current = (list)malloc(sizeof(struct _listnode));
    current = L;
    printf("(");
    while (current != NULL) {
        printlist(current->el);
        current = current->next;

    }

    printf(")\n");

    printf("%c\n", car(lasel(L)).a);

    list current2 = (list)malloc(sizeof(struct _listnode));
    current2 = cdr(lasel(L));
    printf("(");
    while (current2 != NULL) {
        printlist(current2->el);
        current2 = current2->next;

    }
    printf(")\n");
    printlist(car(car(lasel(L))));

    freelist(L);
    freelist(L2);
    freelist(LB);
    freelist(LC);
    freelist(LD);
    freelist(LE);
    freelist(current);
    freelist(current2);

    return 0;





    //---------element L2--------------//
    //element L2;
    // L2.listptr = L; //element.next=List L
     //element * l2 = &l;
    //L2.type = LIST; //L2= LIST
    //---------elemeent e----------------//
    //element e;
    //e.a = 'e';
    //e.type = ATOM;
    //-------------element d------------------//
    //element d;
    //d.a = 'd';
    //d.type = ATOM;

    // L2.listptr=cons(d,cons(e, L)); //retruns the rest of the list minus the head
   // printf("Cons is:", cons(e, L));

    //cons(d, L); //retruns the rest of the list minus the head

     //printf("hello");
     //printf("%c", e.a);
    //printf("hello");
    // printlist(e);
     //printlist(d);
    // L2.type->el= ATOM;
    // printlist(L2);


}

element aasel(atom a) { //atom -> type char
    element content;
    content.type = ATOM; //setting element to be type atom
    content.a = a;
    return content;

}

element lasel(list l) {
    element data;
    data.type = LIST; //setting element to be type list
    data.listptr = l;
    return data; //returns the content as a LIST
}

element car(element e) {
    if (e.type != LIST) {
        return NIL;
    }
    e.listptr->el.type = ATOM;
    return e.listptr->el; //e.next points to next node //SUPPOSED TO POINT TO HEAD
}

list cdr(element e) {
    if (e.type != LIST || e.listptr == NULL) { //if e is not a LIST or if e.next == null
        return NULL;
    }

    return e.listptr->next; //returns the tail of the list
}

list cddr(element e) {
    return cdr(lasel(cdr(e)));
}

list cons(element e, list L) {
    list first_element = (list)malloc(sizeof(struct _listnode));//initializing a list

    first_element->el = car(e);  //first element points to element = head
    first_element->next = L; //first_element.next = List, SHOULDNT IT BE first_element->next= cdr(e) ...????

    return first_element; //returning first element as a list
}

list append(list l1, list l2) {
    list newList = NULL;

    //list it = l1;
    while (l1 != NULL) {
        insert(&newList, l1->el);
        l1 = l1->next;
    }

    // list it2 = l2;
    while (l2 != NULL) {
        insert(&newList, l2->el);
        l2 = l2->next;
    }

    return newList;
}
void freelist(list l1) {
    // list it = l;

    while (l1 != NULL) {
        if (l1->el.type == LIST) {
            freelist(l1->el.listptr);
        }

        list temp = l1->next;
        free((void*)l1);
        l1 = temp;
    }
}
void printlist(element e) {
    if (e.type == LIST && e.listptr == NULL) { //if its an empty list
        printf(" NIL ");
        return;
    }
    else if (e.type == ATOM) {
        printf(" %c ", e.a); //print the data
    }
    else if (e.type == LIST && e.listptr != NULL) {
        list current = e.listptr;//current=e.next
        printf("( ");
        while (current != NULL) {
            printlist(current->el); //print next node el->element of the list
            current = current->next; //moves pointer to next node
        }
        printf(" )");
    }
}

void insert(list* root, element item) {
    list temp = (list)malloc(sizeof(struct _listnode));
    list ptr;
    temp->el = item;
    temp->next = NULL;

    if (*root == NULL)
        *root = temp;
    else {
        ptr = *root;
        while (ptr->next != NULL)
            ptr = ptr->next;
        ptr->next = temp;
    }
}
