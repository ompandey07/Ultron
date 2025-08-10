"""
🤖 Ultron Website Analyzer
Advanced website performance analyzer and optimizer

This package provides comprehensive website analysis including:
- Performance metrics and optimization suggestions
- Security header analysis
- SEO analysis and recommendations
- Broken link detection
- Image optimization analysis
- Mobile-friendliness testing
- Professional Excel, JSON, and HTML reporting

Example:
    >>> from ultron import UltronAnalyzer
    >>> analyzer = UltronAnalyzer()
    >>> results = analyzer.run_comprehensive_check('https://example.com')
    >>> analyzer.print_results(results)
"""

__version__ = "1.2"
__author__ = "Om Pandey"
__email__ = "iamompandey.it@gmail.com"
__license__ = "MIT"

from .analyzer import (
    UltronAnalyzer,
    PerformanceMetrics,
    ImageInfo,
    LinkInfo,
    SEOMetrics,
)

__all__ = [
    "UltronAnalyzer",
    "PerformanceMetrics", 
    "ImageInfo",
    "LinkInfo",
    "SEOMetrics",
]