#!/usr/bin/env python3
"""
Command-line interface for Ultron Website Analyzer
"""

import argparse
import sys
from .analyzer import UltronAnalyzer


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="🤖 Ultron - Advanced Website Performance Analyzer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ultron analyze https://example.com
  ultron analyze https://example.com --format excel
  ultron analyze https://example.com --format all --timeout 60
  ultron --version

Report formats:
  json     - Technical data in JSON format
  html     - Web-friendly HTML report  
  excel    - Professional Excel report (requires openpyxl)
  all      - Generate all format types
  console  - Display results in terminal only
        """
    )
    
    parser.add_argument(
        '--version', 
        action='version', 
        version='Ultron Analyzer v1.0.0'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Analyze command
    analyze_parser = subparsers.add_parser(
        'analyze', 
        help='Analyze a website performance'
    )
    
    analyze_parser.add_argument(
        'url',
        help='Website URL to analyze (e.g., https://example.com)'
    )
    
    analyze_parser.add_argument(
        '--format',
        choices=['console', 'json', 'html', 'excel', 'all'],
        default='console',
        help='Report format (default: console)'
    )
    
    analyze_parser.add_argument(
        '--timeout',
        type=int,
        default=30,
        help='Request timeout in seconds (default: 30)'
    )
    
    analyze_parser.add_argument(
        '--workers',
        type=int,
        default=10,
        help='Maximum concurrent workers (default: 10)'
    )
    
    analyze_parser.add_argument(
        '--suggestions',
        action='store_true',
        help='Show detailed performance suggestions'
    )
    
    analyze_parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress progress output'
    )
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    if args.command == 'analyze':
        run_analysis(args)


def run_analysis(args):
    """Run website analysis with given arguments"""
    url = args.url
    
    # Validate and format URL
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    if not args.quiet:
        print("🤖" * 60)
        print("🚀 ULTRON - ADVANCED SITE PERFORMANCE ANALYZER 🚀") 
        print("🤖" * 60)
        print(f"🔍 Analyzing: {url}")
        print("⚡ Sit back and watch the magic happen...")
        print("=" * 60)
    
    try:
        # Initialize analyzer
        analyzer = UltronAnalyzer(
            timeout=args.timeout,
            max_workers=args.workers
        )
        
        # Run analysis
        results = analyzer.run_comprehensive_check(url)
        
        # Print results to console
        if args.format in ['console', 'all']:
            analyzer.print_results(results)
        
        # Generate reports
        if args.format == 'json' or args.format == 'all':
            analyzer.save_report(results, 'json')
        
        if args.format == 'html' or args.format == 'all':
            analyzer.save_report(results, 'html')
        
        if args.format == 'excel' or args.format == 'all':
            try:
                analyzer.save_report(results, 'excel')
            except ImportError:
                print("⚠️ Excel format requires openpyxl. Install with: pip install ultron-analyzer[excel]")
                if args.format == 'excel':
                    print("📄 Generating JSON report instead...")
                    analyzer.save_report(results, 'json')
        
        # Show performance suggestions if requested
        if args.suggestions:
            suggestions = analyzer.generate_performance_suggestions(results)
            analyzer.print_performance_suggestions(suggestions)
        
        # Summary
        if not args.quiet:
            perf = results['performance']
            insights_count = len(results['insights'])
            
            print(f"\n🤖 ULTRON ANALYSIS COMPLETE!")
            print("=" * 40)
            print(f"   ⚡ Load Time: {perf['total_time']:.2f}s")
            print(f"   📦 Page Size: {perf['page_size'] / 1024:.1f}KB")
            print(f"   💡 Issues Found: {insights_count}")
            
            if insights_count == 0:
                print(f"\n🏆 PERFECT SCORE! Your site is optimized!")
            elif insights_count <= 3:
                print(f"\n🥇 EXCELLENT! Minor tweaks for perfection")
            elif insights_count <= 6:
                print(f"\n🥈 GOOD! Some optimizations needed")
            else:
                print(f"\n🥉 NEEDS WORK! Multiple improvements required")
            
            print(f"\n💡 Run with --suggestions for detailed optimization tips")
    
    except Exception as e:
        print(f"\n❌ Error analyzing {url}: {e}")
        print("\n🔍 This might be due to:")
        print("   • Website is down or unreachable")
        print("   • Network connectivity issues")
        print("   • Website blocking automated requests")
        print("   • Invalid URL format")
        sys.exit(1)


if __name__ == '__main__':
    main()