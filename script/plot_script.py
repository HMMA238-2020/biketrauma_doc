"""
This is my example-script
==========================

This example doesn't do much, it just makes a simple plot
"""

import biketrauma

df = biketrauma.Load_db().save_as_df()
biketrauma.plot_location(biketrauma.get_accident(df))
