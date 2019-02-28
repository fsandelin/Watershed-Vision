from matplotlib import cm

def create_colorMap(color_map = "tab10"):
  color_map_func = getattr(cm, color_map)
  return [tuple(map(lambda x: x*255, color_map_func(i)[:3])) for i in range(10)]