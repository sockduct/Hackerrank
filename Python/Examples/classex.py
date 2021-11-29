class MyClass:
    # Class variable
    cvar = 'a'

    def __init__(self, num=0):
        # Instance variable
        self.ivar = num

    def __repr__(self):
        return f'MyClass({self.ivar})'

    def method(self):
        # Normal class method - requires instance
        # Operates within instance namespace
        # Class namespace accessible through .__class__
        mtype = 'instance'

        '''
        * From here, if access self.cvar and there's no instance variable "cvar"
          then we walk up to the class level and access it
        * If we do self.cvar = 'x' - this creates an instance variable which "shadows"
          the class variable
        * To change the class variable we need to do:  self.__class__.cvar = 'x'
        '''

        return (f'{mtype} method called ({self}, cvar={MyClass.cvar}, ivar={self.ivar})'
                f'\n\t(self.__dict__={self.__dict__}'
                f'\n\t(self.__class__.__dict__.keys()={tuple(self.__class__.__dict__.keys())})')

    @classmethod
    def classmethod(cls):
        # Works at class level - doesn't have to create an instance (but can - see below)
        # Operates within class namespace
        mtype = 'class'

        return (f'{mtype} method called ({cls}, cvar={MyClass.cvar}, ivar=inaccessible)'
                f'\n\t(cls.__dict__.keys()={tuple(cls.__dict__.keys())}')

    '''
    # Would have to comment out above method to uncomment these two:
    @classmethod
    def five(cls):
        # Alternate constructor/factory function:
        return cls(5)

    @classmethod
    def fifteen(cls):
        # Alternate constructor/factory function:
        return cls(15)
    '''

    @staticmethod
    def staticmethod():
        # Stand alone method - doesn't take instance/class object
        # Can be used without an instance
        mtype = 'static'

        return (f'{mtype} method called ({staticmethod}, cvar={MyClass.cvar}, ivar=inaccessible)'
                f'\n\t(staticmethod.__dict__.keys()={tuple(staticmethod.__dict__.keys())}')


if __name__ == '__main__':
    c1 = MyClass()
    print(f'c1.method():  {c1.method()}')
    print(f'\nMyClass.method(c1):  {MyClass.method(c1)}')
    print('-' * 72)
    print(f'c1.classmethod():  {c1.classmethod()}')
    print(f'\nMyClass.classmethod(c1):  {MyClass.classmethod()}')
    print('-' * 72)
    print(f'c1.staticmethod():  {c1.staticmethod()}')
    print(f'\nMyClass.staticmethod(c1):  {MyClass.staticmethod()}')
