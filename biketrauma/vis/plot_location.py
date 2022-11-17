import pygal  # First import pygal

# from pygal.maps.fr import aggregate_regions


def plot_location(gd):
    r"""
  The plot_location function plots the data. You may add nicely formatted stuff ``"AL = TYPE(DIM)"`` and maths :
      
      .. math::
          a_i~=~f(x_i)~&=~ \log \sum_{j=1}^{N} \exp(-\gamma\cdot\|x_i-y_j\|^2)\cdot b_j \\\\
             ~&=~ \log \sum_{j=1}^{N} \exp\\big(-\gamma\cdot\|x_i-y_j\|^2 \,+\, \log(b_j) \\big).

  Input
  -----
    gd: I don't remenber the type of gd. 

  Output
  ------
    nothing...

  Example
  -------

  >> import biketrauma
  >> biketrauma.vis.plot_location(blahblha)

  """
    fr_chart = pygal.maps.fr.Departments(human_readable=True)
    fr_chart.title = "Accident by region"

    fr_chart.add("Accidents", gd.to_dict())

    fr_chart.render_in_browser()
    # fr_chart.render_to_file('./chart.svg')  # Write the chart in the specified file
