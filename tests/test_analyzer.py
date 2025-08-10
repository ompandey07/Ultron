#!/usr/bin/env python3
"""
Test suite for Ultron Website Analyzer
"""

import unittest
from unittest.mock import Mock, patch
from ultron import UltronAnalyzer, PerformanceMetrics, SEOMetrics


class TestUltronAnalyzer(unittest.TestCase):
    """Test cases for UltronAnalyzer class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.analyzer = UltronAnalyzer(timeout=10, max_workers=2)
    
    def test_analyzer_initialization(self):
        """Test analyzer initialization"""
        self.assertEqual(self.analyzer.timeout, 10)
        self.assertEqual(self.analyzer.max_workers, 2)
        self.assertIsNotNone(self.analyzer.session)
    
    def test_performance_metrics_creation(self):
        """Test PerformanceMetrics dataclass"""
        metrics = PerformanceMetrics(
            total_time=2.5,
            page_size=1024000,
            status_code=200
        )
        
        self.assertEqual(metrics.total_time, 2.5)
        self.assertEqual(metrics.page_size, 1024000)
        self.assertEqual(metrics.status_code, 200)
    
    def test_seo_metrics_creation(self):
        """Test SEOMetrics dataclass"""
        seo = SEOMetrics(
            title="Test Page",
            meta_description="Test description",
            h1_tags=["Main Heading"],
            images_without_alt=2
        )
        
        self.assertEqual(seo.title, "Test Page")
        self.assertEqual(seo.meta_description, "Test description")
        self.assertEqual(len(seo.h1_tags), 1)
        self.assertEqual(seo.images_without_alt, 2)
    
    @patch('requests.Session.get')
    def test_get_page_performance(self, mock_get):
        """Test page performance measurement"""
        # Mock response
        mock_response = Mock()
        mock_response.content = b"test content"
        mock_response.status_code = 200
        mock_response.elapsed.total_seconds.return_value = 1.5
        mock_get.return_value = mock_response
        
        metrics = self.analyzer.get_page_performance("https://example.com")
        
        self.assertEqual(metrics.status_code, 200)
        self.assertEqual(metrics.page_size, len(b"test content"))
        self.assertGreater(metrics.total_time, 0)
    
    @patch('requests.Session.head')
    def test_check_security_headers(self, mock_head):
        """Test security headers check"""
        # Mock response with some security headers
        mock_response = Mock()
        mock_response.headers = {
            'X-Content-Type-Options': 'nosniff',
            'X-Frame-Options': 'DENY',
            'Strict-Transport-Security': 'max-age=31536000'
        }
        mock_head.return_value = mock_response
        
        headers = self.analyzer.check_security_headers("https://example.com")
        
        self.assertTrue(headers['X-Content-Type-Options'])
        self.assertTrue(headers['X-Frame-Options'])
        self.assertTrue(headers['Strict-Transport-Security'])
        self.assertFalse(headers['Content-Security-Policy'])
    
    def test_generate_insights(self):
        """Test insights generation"""
        # Create test data
        performance = PerformanceMetrics(total_time=5.0, page_size=3000000)
        security = {'X-Frame-Options': False, 'Content-Security-Policy': False}
        seo = SEOMetrics(title="", images_without_alt=3)
        images = []
        links = []
        mobile = {'viewport_meta': False}
        
        insights = self.analyzer.generate_insights(
            performance, security, seo, images, links, mobile
        )
        
        # Check that insights are generated for various issues
        self.assertTrue(any("CRITICAL" in insight for insight in insights))
        self.assertTrue(any("security headers" in insight for insight in insights))
        self.assertTrue(any("Missing page title" in insight for insight in insights))
        self.assertTrue(any("viewport meta tag" in insight for insight in insights))


class TestCLI(unittest.TestCase):
    """Test cases for CLI functionality"""
    
    def test_import_cli(self):
        """Test that CLI module can be imported"""
        try:
            from ultron.cli import main
            self.assertTrue(callable(main))
        except ImportError:
            self.fail("Failed to import CLI module")


if __name__ == '__main__':
    unittest.main()