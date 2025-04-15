""" 
    @Author: Franco Lionti
    @version: 0.1.0
    @date: 15/04/2025
    @description: 
"""

# __init__.py
from .audio_processor import AudioProcessor
from .techniques import *
from .evaluation import QualityEvaluator, ScoreCalculator
from .diagnostic import DiagnosticEngine

__version__ = '0.1.0'