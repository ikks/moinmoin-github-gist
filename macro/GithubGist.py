# -*- coding: utf-8 -*-
# Author: Igor Támara igor@tamarapatino.org
# Date: 14/09/2015
# No warranties.
"""
  MoinMoin - Gist github
  Embeds a gist github inside moinmoin

  Inputs: Receieves a Github URL containing a gist

  For instance:
  <<GithubGist(https://gist.github.com/ikks/0075a7bcf8fe526ab4c3)>>

  would show the given gist using the Embed URL.

"""


def execute(macro, args):
    if not args.startswith('https://gist.github.com/'):
        return "you must offer something that starts with https://gist.github."
    return macro.formatter.rawHTML(
        '<script src="{0}.js"></script>'.format(args)
    )
