import click
import utilities

@click.group()
def cli():
    ''' Wolfenstien 3D Cheat Engine '''
    pass


@cli.command()
def GiveMoreAmmo():
    ''' Give the player more ammo '''
    utilities.Get_Ammo()
    utilities.AddAmmo(quantity=50)
    utilities.Get_Ammo()

@cli.command()
def GiveScorePoints():
    ''' Update the score for the player '''
    utilities.Get_Score()
    utilities.AddScore(quantity=1000)
    utilities.Get_Score()

@cli.command()
def GiveHealth():
    ''' Gives the player more health '''
    utilities.Get_Health()
    utilities.AddHealth(quantity=50)
    utilities.Get_Health()

if __name__=="__main__":
    cli()
