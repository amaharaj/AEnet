#!/bin/bash

rename 's/\d+/sprintf("%06d", $&)/e' output*

