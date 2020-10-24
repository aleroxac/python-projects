#!/usr/bin/env python3
#encoding=utf8

# NAME: pydo
# DESCRIPTION: Command line utility to setting up yours tasks.
# AUTHOR: Augusto Cardoso dos Santos
# DATE: 25/04/2019
# CHANGELOG: 
#    - 25/04/2019: Criação do programa


from datetime import datetime, timedelta


#---------- CLASSES
class TaskNotFound(Exception):
    pass

class Project():
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def _add_task(self, task, **kwargs): # intern method
        self.tasks.append(task)

    def _add_task_by_description(self, description, **kwargs): # intern method
        self.tasks.append(Task(description, kwargs.get('duedate', None)))

    def add(self,task, duedate=None, **kwargs): # function overflow simulation
        choiced_function_to_add_task = self._add_task if isinstance(task, Task)\
            else self._add_task_by_description
        kwargs['duedate'] = duedate
        choiced_function_to_add_task(task, **kwargs)

    def pendents(self):
        return [task for task in self.tasks if not task.done]

    def search(self, description):
        try:
            return [task for task in self.tasks if task.description == description][0]
        except IndexError as error:
            raise TaskNotFound(str(error))

    def __str__(self): # When the object is printed
        return f'{self.name}: {len(self.pendents())} pending(s) task(s)'

    def __iter__(self): # When the object is iterated
        return self.tasks.__iter__()

    def __iadd__(self, task): # to grant that owners can be have tasks
        task.owner =  self
        self._add_task(task)
        return self



class Task:
    def __init__(self, description, duedate=None):
        self.description = description
        self.done = False
        self.creation = datetime.now()
        self.duedate = duedate

    def complete(self):
        self.done = True

    def __str__(self):
        status = []
        if self.done:
            status.append('[COMPLETED]')
        elif self.duedate:
            if datetime.now() > self.duedate:
                status.append('[EXPIRED]')
            else:
                days = (self.duedate - datetime.now()).days
                status.append(f'[Expires in {days} day(s)]')

        return f'{self.description} ' + ''.join(status)

class RecurringTask(Task):
    def __init__(self, description, duedate, days=7):
        super().__init__(description, duedate)
        self.days = days
        self.owner = None

    def complete(self):
        super().complete()
        new_duedate = datetime.now() + timedelta(days=self.days)
        new_task = RecurringTask(self.description, new_duedate, self.days)
        if self.owner:
            self.owner += new_task
        return new_task


#---------- FUNCTIONS
def main():
    home = Project('Tarefas de casa')
    home.add('Passar roupa', datetime.now())
    home.add('Lavar prato')
    home += RecurringTask('Trocar lençóis', datetime.now(), 7)
    home.search('Trocar lençóis').complete()
    print(home)

    try:
        home.search('Lavar prato - ERRO').complete()
    except TaskNotFound as error:
        print(f'Causa do erro: "{str(error)}"')

    home.search('Lavar prato').complete()
    for task in home:
        print(f'- {task}')
    print(home)


    market = Project('Compras no mercado')
    market.add('Frutas secas')
    market.add('Carne')
    market.add('Tomate', datetime.now() + timedelta(days=3, minutes=12))
    print(market)

    market.search('Carne').complete()
    for task in market:
        print(f'- {task}')
    print(market)


#---------- MAIN
if __name__ == '__main__':
    main()
