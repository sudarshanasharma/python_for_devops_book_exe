###Create a CLI with click that takes a name as argument, and prints it if it starts with p
#!/usr/bin/env python

import click
import re
@click.command()
@click.option('--name',default='Pamsam',help='what izs your name?')
def print_p_name(name):
  if re.match(r'(^[Pp]\w+)',name):
    print(f"{name}")
  
  
if __name__=='__main__':
  print_p_name()
