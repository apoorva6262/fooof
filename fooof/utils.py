"""Public utility & helper functions for FOOOF."""

import numpy as np

from fooof.synth import gen_freqs
from fooof.core.utils import get_obj_desc

###################################################################################################
###################################################################################################

def trim_spectrum(freqs, power_spectra, f_range):
    """Extract frequency range of interest from power spectra.

    Parameters
    ----------
    freqs : 1d array
        Frequency values for the PSD.
    power_spectra : 1d or 2d array
        Power spectral density values.
    f_range: list of [float, float]
        Frequency range to restrict to.

    Returns
    -------
    freqs_ext : 1d array
        Extracted frequency values for the power spectrum.
    power_spectra_ext : 1d or 2d array
        Extracted power spectral density values.

    Notes
    -----
    This function extracts frequency ranges >= f_low and <= f_high.
    It does not round to below or above f_low and f_high, respectively.
    """

    # Create mask to index only requested frequencies
    f_mask = np.logical_and(freqs >= f_range[0], freqs <= f_range[1])

    # Restrict freqs & psd to requested range. The if/else is to cover both 1d or 2d arrays
    freqs_ext = freqs[f_mask]
    power_spectra_ext = power_spectra[f_mask] if power_spectra.ndim == 1 \
        else power_spectra[:, f_mask]

    return freqs_ext, power_spectra_ext


def get_info(f_obj, aspect):
    """

    Parameters
    ----------
    f_obj : FOOOF or FOOOFGroup
        FOOOF derived object to get attributes from.
    aspect : {'settings', 'data_info', 'results'}
        Which set of attributes to compare the objects across.

    Returns
    -------
    dict
        xx
    """

    return {key : getattr(f_obj, key) for key in get_obj_desc()[aspect]}


def compare_info(lst, aspect):
    """Compare a specified aspect of FOOOF objects across instances.

    Parameters
    ----------
    lst : list of FOOOF or FOOOFGroup objects
        FOOOF related objects whose attibutes are to be compared.
    aspect : {'setting', 'data_info'}
        Which set of attributes to compare the objects across.

    Returns
    -------
    consistent : bool
        Whether the settings are consistent across the input list of objects.
    """

    # Check specified aspect of the objects are the same across instances
    for f_obj_1, f_obj_2 in zip(lst[:-1], lst[1:]):
        if getattr(f_obj_1, 'get_' + aspect)() != getattr(f_obj_2, 'get_' + aspect)():
            consistent = False
            break
    else:
        consistent = True

    return consistent





# def get_settings(f_obj):
#     """Get a dictionary of current settings from a FOOOF or FOOOFGroup object.

#     Parameters
#     ----------
#     f_obj : FOOOF or FOOOFGroup
#         FOOOF derived object to get settings from.

#     Returns
#     -------
#     dictionary
#         Settings for the input FOOOF derived object.
#     """

#     return {setting : getattr(f_obj, setting) for setting in get_obj_desc()['settings']}


# def get_data_info(f_obj):
#     """Get a dictionary of current data information from a FOOOF or FOOOFGroup object.

#     Parameters
#     ----------
#     f_obj : FOOOF or FOOOFGroup
#         FOOOF derived object to get data information from.

#     Returns
#     -------
#     dictionary
#         Data information for the input FOOOF derived object.

#     Notes
#     -----
#     Data information for a FOOOF object is the frequency range and frequency resolution.
#     """

#     return {dat_info : getattr(f_obj, dat_info) for dat_info in get_obj_desc()['data_info']}


# def compare_settings(lst):
#     """Compare the settings between FOOOF and/or FOOOFGroup objects.

#     Parameters
#     ----------
#     lst : list of FOOOF or FOOOFGroup objects
#         FOOOF related objects whose settings are to be compared.

#     Returns
#     -------
#     consistent : bool
#         Whether the settings are consistent across the input list of objects.
#     """

#     # Check settings are the same across list of given objects
#     for f_obj_1, f_obj_2 in zip(lst[:-1], lst[1:]):
#         if f_obj_1.get_settings() != f_obj_2.get_settings():
#             consistent = False
#             break
#     else:
#         consistent = True

#     return consistent


# def compare_data_info(lst):
#     """Compare the data information between FOOOF and/or FOOOFGroup objects.

#     Parameters
#     ----------
#     lst : list of FOOOF or FOOOFGroup objects
#         FOOOF related objects whose settings are to be compared.

#     Returns
#     -------
#     consistent : bool
#         Whether the data information is consistent across the input list of objects.

#     Notes
#     -----
#     Data information for a FOOOF object is the frequency range and frequency resolution.
#     """

#     # Check data information is the same across the list of given objects
#     for f_obj_1, f_obj_2 in zip(lst[:-1], lst[1:]):
#         if get_data_info(f_obj_1) != get_data_info(f_obj_2):
#             consistent = False
#             break
#     else:
#         consistent = True

#     return consistent
