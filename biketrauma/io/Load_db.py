import os
import pandas as pd
import pooch
from biketrauma.io import url_db, path_target
import lzma


class Load_db:
    """
    This class download the compressed biketrauma dataset.
    """

    def __init__(self, url=url_db, target_name=path_target):
        """
        Parameters
        ----------

        url : (string) path to the data

        target_name : (string) local path where data is saved
        """
        path, fname_compressed = os.path.split(path_target)
        pooch.retrieve(url, path=path, fname=fname_compressed, known_hash=None)
        self.fname = self.unxz(path_target)

    def unxz(self, fname_compressed):
        """
        Uncompress the xz file

        Parameters
        ----------

        fname_compressed : (string) name of the compressed file

        Returns
        -------
        
        fname_uncompressed : (string) name of the uncompressed file

        """
        fname_uncompressed = fname_compressed[:-3]
        if os.path.exists(fname_uncompressed):
            return fname_uncompressed

        # read the compressed file
        with lzma.open(fname_compressed) as f:
            file_content = f.read().decode('utf-8')

            # write the string file_content to a file named fname_uncompressed
            with open(fname_uncompressed, 'w') as f:
                f.write(file_content)

        return fname_uncompressed


    def save_as_df(self):
        """
        Import data to a Pandas :class:`pandas.DataFrame`. See <https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>
        """
        df_bikes = pd.read_csv(
            self.fname,
            na_values="",
            low_memory=False,
            converters={"data": str, "heure": str},
        )
        return df_bikes
