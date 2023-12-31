# coding=utf-8
# Copyright 2023 The Dopamine Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Human and random Atari scores, and a function to normalization by them."""

ATARI_HUMAN_SCORES = {
    'alien': 7127.7,
    'amidar': 1719.5,
    'assault': 742.0,
    'asterix': 8503.3,
    'asteroids': 47388.7,
    'atlantis': 29028.1,
    'bankheist': 753.1,
    'battlezone': 37187.5,
    'beamrider': 16926.5,
    'berzerk': 2630.4,
    'bowling': 160.7,
    'boxing': 12.1,
    'breakout': 30.5,
    'centipede': 12017.0,
    'choppercommand': 7387.8,
    'crazyclimber': 35829.4,
    'demonattack': 1971.0,
    'doubledunk': -16.4,
    'enduro': 860.5,
    'fishingderby': -38.7,
    'freeway': 29.6,
    'frostbite': 4334.7,
    'gopher': 2412.5,
    'gravitar': 3351.4,
    'hero': 30826.4,
    'icehockey': 0.9,
    'jamesbond': 302.8,
    'kangaroo': 3035.0,
    'krull': 2665.5,
    'kungfumaster': 22736.3,
    'montezumarevenge': 4753.3,
    'mspacman': 6951.6,
    'namethisgame': 8049.0,
    'phoenix': 7242.6,
    'pitfall': 6463.7,
    'pong': 14.6,
    'privateeye': 69571.3,
    'qbert': 13455.0,
    'riverraid': 17118.0,
    'roadrunner': 7845.0,
    'robotank': 11.9,
    'seaquest': 42054.7,
    'skiing': -4336.9,
    'solaris': 12326.7,
    'spaceinvaders': 1668.7,
    'stargunner': 10250.0,
    'tennis': -8.3,
    'timepilot': 5229.2,
    'tutankham': 167.6,
    'upndown': 11693.2,
    'venture': 1187.5,
    'videopinball': 17667.9,
    'wizardofwor': 4756.5,
    'yarsrevenge': 54576.9,
    'zaxxon': 9173.3,
}

ATARI_RANDOM_SCORES = {
    'alien': 227.8,
    'amidar': 5.8,
    'assault': 222.4,
    'asterix': 210.0,
    'asteroids': 719.1,
    'atlantis': 12850.0,
    'bankheist': 14.2,
    'battlezone': 2360.0,
    'beamrider': 363.9,
    'berzerk': 123.7,
    'bowling': 23.1,
    'boxing': 0.1,
    'breakout': 1.7,
    'centipede': 2090.9,
    'choppercommand': 811.0,
    'crazyclimber': 10780.5,
    'defender': 2874.5,
    'demonattack': 152.1,
    'doubledunk': -18.6,
    'enduro': 0.0,
    'fishingderby': -91.7,
    'freeway': 0.0,
    'frostbite': 65.2,
    'gopher': 257.6,
    'gravitar': 173.0,
    'hero': 1027.0,
    'icehockey': -11.2,
    'jamesbond': 29.0,
    'kangaroo': 52.0,
    'krull': 1598.0,
    'kungfumaster': 258.5,
    'montezumarevenge': 0.0,
    'mspacman': 307.3,
    'namethisgame': 2292.3,
    'phoenix': 761.4,
    'pitfall': -229.4,
    'pong': -20.7,
    'privateeye': 24.9,
    'qbert': 163.9,
    'riverraid': 1338.5,
    'roadrunner': 11.5,
    'robotank': 2.2,
    'seaquest': 68.4,
    'skiing': -17098.1,
    'solaris': 1236.3,
    'spaceinvaders': 148.0,
    'stargunner': 664.0,
    'surround': -10.0,
    'tennis': -23.8,
    'timepilot': 3568.0,
    'tutankham': 11.4,
    'upndown': 533.4,
    'venture': 0.0,
    'videopinball': 0.0,
    'wizardofwor': 563.5,
    'yarsrevenge': 3092.9,
    'zaxxon': 32.5,
}


def normalize_score(ret, game):
  return (ret - ATARI_RANDOM_SCORES[game]) / (
      ATARI_HUMAN_SCORES[game] - ATARI_RANDOM_SCORES[game]
  )
