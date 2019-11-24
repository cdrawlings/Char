from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class NewUser(FlaskForm):
    """new User form."""
    name = StringField('name', validators=[DataRequired()])
    lastname = StringField('Last name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    submit = SubmitField('Submit')


class NewChar(FlaskForm):
    """new User form."""
    charname = StringField('Character Name', validators=[DataRequired()])
    charclass = SelectField('Select Class',
                            choices=[('barb', 'Barbarian'), ('bard', 'Bard'), ('cleric', 'Cleric',), ('druid', 'Druid'),
                                     ('fighter', 'Fighter'), ('monk', 'Monk'), ('paladin', 'Paladin'),
                                     ('ranger', 'Ranger'), ('rogue', 'Rogue'), ('sorcerer', 'Sorcerer'),
                                     ('warlock', 'Warlock'), ('wizard', 'Wizaed')], validators=[DataRequired()])
    charalign = SelectField('Alignment',
                            choices=[('alignlg', 'Lawful Good'), ('alignng', 'Neutral Good'),
                                     ('aligncg', 'Chaotic Good',), ('alignng', 'Lawful Neutral'),
                                     ('alignTN', 'True Neutral'), ('aligncn', 'Chaotic Neutral',),
                                     ('alignle', 'Lawful Evil'), ('alignne', 'Neutral Evil'),
                                     ('alignce', 'Chaotic Evil',)])

    charrace = SelectField('Select Class',
                           choices=[('dborn', 'Dragonborn'), ('hdwarf', 'Dwarf, Hill'), ('mdwarf', 'Dwarf, Mountain'),
                                    ('helf', 'Elf, High'), ('welf', 'Elf, Wood'), ('fgnome', 'Gnome, Forest'),
                                    ('rgnome', 'Gnome, Rock'), ('lhalf', 'Halfling, lightfoot'),
                                    ('shalf', 'Halfling, Stout'), ('helf', 'Half Elf'), ('horc', 'Half Orc'),
                                    ('human', 'Human'), ('tief', 'Tiefling')], validators=[DataRequired()])
    charbkgrd = SelectField('Select Class',
                            choices=[('acolyte', 'Acolyte',), ('charlatan', 'Charlatan'), ('criminal', 'Criminal'),
                                     ('entertainer', 'Entertainer'), ('fhero', 'Folk Hero'),
                                     ('gartisan', 'Guild Artisan'), ('hermit', 'Hermit'), ('nobel', 'Nobel'),
                                     ('outlander', 'Outlander'), ('sage', 'Sage'), ('sailor', 'Sailor'),
                                     ('soldier', 'Soldier'), ('urchin', 'Urchin')], validators=[DataRequired()])
    charlevel = StringField('Character Level', default='01', validators=[DataRequired()])
    submit = SubmitField('Submit')
