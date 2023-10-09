"""
This is my example-script
==========================

This example doesn't do much, it just makes a simple plot


.. raw:: html

    <iframe frameborder=0  width=100% height=600 src="../../../images/biketrauma_map.svg"></iframe>

"""
import biketrauma


df = biketrauma.Load_db().save_as_df()
biketrauma.plot_location(biketrauma.get_accident(df))
