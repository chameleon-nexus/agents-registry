#!/usr/bin/env python3
"""
Translate agent names and descriptions to Chinese and Japanese
"""

import os
import json
from pathlib import Path

# Translation mappings for common programming terms and agent types
TRANSLATIONS = {
    # Programming languages
    "python-pro": {
        "zh": "Python 专家",
        "ja": "Python プロ"
    },
    "javascript-pro": {
        "zh": "JavaScript 专家", 
        "ja": "JavaScript プロ"
    },
    "typescript-pro": {
        "zh": "TypeScript 专家",
        "ja": "TypeScript プロ"
    },
    "java-pro": {
        "zh": "Java 专家",
        "ja": "Java プロ"
    },
    "golang-pro": {
        "zh": "Go 专家",
        "ja": "Go プロ"
    },
    "rust-pro": {
        "zh": "Rust 专家", 
        "ja": "Rust プロ"
    },
    "cpp-pro": {
        "zh": "C++ 专家",
        "ja": "C++ プロ"
    },
    "csharp-pro": {
        "zh": "C# 专家",
        "ja": "C# プロ"
    },
    "php-pro": {
        "zh": "PHP 专家",
        "ja": "PHP プロ"
    },
    "ruby-pro": {
        "zh": "Ruby 专家",
        "ja": "Ruby プロ"
    },
    "scala-pro": {
        "zh": "Scala 专家",
        "ja": "Scala プロ"
    },
    "sql-pro": {
        "zh": "SQL 专家",
        "ja": "SQL プロ"
    },
    "c-pro": {
        "zh": "C 专家",
        "ja": "C プロ"
    },
    "elixir-pro": {
        "zh": "Elixir 专家",
        "ja": "Elixir プロ"
    },
    
    # Frameworks and tools
    "django-pro": {
        "zh": "Django 专家",
        "ja": "Django プロ"
    },
    "fastapi-pro": {
        "zh": "FastAPI 专家", 
        "ja": "FastAPI プロ"
    },
    "flutter-expert": {
        "zh": "Flutter 专家",
        "ja": "Flutter エキスパート"
    },
    
    # Roles and specializations
    "ai-engineer": {
        "zh": "AI 工程师",
        "ja": "AI エンジニア"
    },
    "backend-architect": {
        "zh": "后端架构师",
        "ja": "バックエンドアーキテクト"
    },
    "frontend-developer": {
        "zh": "前端开发工程师", 
        "ja": "フロントエンド開発者"
    },
    "mobile-developer": {
        "zh": "移动开发工程师",
        "ja": "モバイル開発者"
    },
    "ios-developer": {
        "zh": "iOS 开发工程师",
        "ja": "iOS 開発者"
    },
    "data-engineer": {
        "zh": "数据工程师",
        "ja": "データエンジニア"
    },
    "data-scientist": {
        "zh": "数据科学家",
        "ja": "データサイエンティスト"
    },
    "ml-engineer": {
        "zh": "机器学习工程师",
        "ja": "機械学習エンジニア"
    },
    "mlops-engineer": {
        "zh": "MLOps 工程师",
        "ja": "MLOps エンジニア"
    },
    "devops-troubleshooter": {
        "zh": "DevOps 故障排除专家",
        "ja": "DevOps トラブルシューター"
    },
    "cloud-architect": {
        "zh": "云架构师",
        "ja": "クラウドアーキテクト"
    },
    "hybrid-cloud-architect": {
        "zh": "混合云架构师",
        "ja": "ハイブリッドクラウドアーキテクト"
    },
    "kubernetes-architect": {
        "zh": "Kubernetes 架构师",
        "ja": "Kubernetes アーキテクト"
    },
    "security-auditor": {
        "zh": "安全审计专家",
        "ja": "セキュリティ監査者"
    },
    "backend-security-coder": {
        "zh": "后端安全编程专家",
        "ja": "バックエンドセキュリティコーダー"
    },
    "frontend-security-coder": {
        "zh": "前端安全编程专家", 
        "ja": "フロントエンドセキュリティコーダー"
    },
    "mobile-security-coder": {
        "zh": "移动安全编程专家",
        "ja": "モバイルセキュリティコーダー"
    },
    "database-admin": {
        "zh": "数据库管理员",
        "ja": "データベース管理者"
    },
    "database-optimizer": {
        "zh": "数据库优化专家",
        "ja": "データベース最適化専門家"
    },
    "network-engineer": {
        "zh": "网络工程师",
        "ja": "ネットワークエンジニア"
    },
    "performance-engineer": {
        "zh": "性能工程师",
        "ja": "パフォーマンスエンジニア"
    },
    "observability-engineer": {
        "zh": "可观测性工程师",
        "ja": "オブザーバビリティエンジニア"
    },
    "deployment-engineer": {
        "zh": "部署工程师",
        "ja": "デプロイメントエンジニア"
    },
    "incident-responder": {
        "zh": "事件响应专家",
        "ja": "インシデント対応者"
    },
    "terraform-specialist": {
        "zh": "Terraform 专家",
        "ja": "Terraform スペシャリスト"
    },
    
    # Testing and debugging
    "debugger": {
        "zh": "调试专家",
        "ja": "デバッガー"
    },
    "error-detective": {
        "zh": "错误检测专家",
        "ja": "エラー探偵"
    },
    "test-automator": {
        "zh": "测试自动化专家",
        "ja": "テスト自動化専門家"
    },
    "tdd-orchestrator": {
        "zh": "TDD 编排专家",
        "ja": "TDD オーケストレーター"
    },
    
    # Documentation and content
    "api-documenter": {
        "zh": "API 文档专家",
        "ja": "API ドキュメンテーター"
    },
    "docs-architect": {
        "zh": "文档架构师",
        "ja": "ドキュメントアーキテクト"
    },
    "tutorial-engineer": {
        "zh": "教程工程师",
        "ja": "チュートリアルエンジニア"
    },
    "content-marketer": {
        "zh": "内容营销专家",
        "ja": "コンテンツマーケター"
    },
    "prompt-engineer": {
        "zh": "提示词工程师",
        "ja": "プロンプトエンジニア"
    },
    
    # Code quality and review
    "code-reviewer": {
        "zh": "代码审查专家",
        "ja": "コードレビュアー"
    },
    "architect-review": {
        "zh": "架构评审专家",
        "ja": "アーキテクチャレビュアー"
    },
    "legacy-modernizer": {
        "zh": "遗留系统现代化专家",
        "ja": "レガシーモダナイザー"
    },
    "dx-optimizer": {
        "zh": "开发体验优化专家", 
        "ja": "DX最適化専門家"
    },
    
    # Business and management
    "business-analyst": {
        "zh": "业务分析师",
        "ja": "ビジネスアナリスト"
    },
    "hr-pro": {
        "zh": "人力资源专家",
        "ja": "人事プロ"
    },
    "customer-support": {
        "zh": "客户支持专家",
        "ja": "カスタマーサポート"
    },
    "sales-automator": {
        "zh": "销售自动化专家",
        "ja": "セールス自動化専門家"
    },
    "legal-advisor": {
        "zh": "法律顾问",
        "ja": "法的アドバイザー"
    },
    "risk-manager": {
        "zh": "风险管理专家",
        "ja": "リスクマネージャー"
    },
    "quant-analyst": {
        "zh": "量化分析师",
        "ja": "クオンツアナリスト"
    },
    
    # Design and UX
    "ui-ux-designer": {
        "zh": "UI/UX 设计师",
        "ja": "UI/UX デザイナー"
    },
    "ui-visual-validator": {
        "zh": "UI 视觉验证专家",
        "ja": "UI ビジュアル検証者"
    },
    
    # Specialized tools
    "blockchain-developer": {
        "zh": "区块链开发工程师",
        "ja": "ブロックチェーン開発者"
    },
    "unity-developer": {
        "zh": "Unity 开发工程师",
        "ja": "Unity 開発者"
    },
    "minecraft-bukkit-pro": {
        "zh": "Minecraft Bukkit 专家",
        "ja": "Minecraft Bukkit プロ"
    },
    "graphql-architect": {
        "zh": "GraphQL 架构师",
        "ja": "GraphQL アーキテクト"
    },
    "payment-integration": {
        "zh": "支付集成专家",
        "ja": "決済統合専門家"
    },
    "search-specialist": {
        "zh": "搜索专家",
        "ja": "検索スペシャリスト"
    },
    "context-manager": {
        "zh": "上下文管理专家",
        "ja": "コンテキストマネージャー"
    },
    "reference-builder": {
        "zh": "参考资料构建专家",
        "ja": "リファレンスビルダー"
    },
    "mermaid-expert": {
        "zh": "Mermaid 图表专家",
        "ja": "Mermaid エキスパート"
    },
    
    # SEO specialists
    "seo-authority-builder": {
        "zh": "SEO 权威建设专家",
        "ja": "SEO オーソリティビルダー"
    },
    "seo-cannibalization-detector": {
        "zh": "SEO 竞争检测专家",
        "ja": "SEO カニバリゼーション検出器"
    },
    "seo-content-auditor": {
        "zh": "SEO 内容审计专家",
        "ja": "SEO コンテンツ監査者"
    },
    "seo-content-planner": {
        "zh": "SEO 内容规划专家",
        "ja": "SEO コンテンツプランナー"
    },
    "seo-content-refresher": {
        "zh": "SEO 内容更新专家",
        "ja": "SEO コンテンツリフレッシャー"
    },
    "seo-content-writer": {
        "zh": "SEO 内容撰写专家",
        "ja": "SEO コンテンツライター"
    },
    "seo-keyword-strategist": {
        "zh": "SEO 关键词策略专家",
        "ja": "SEO キーワードストラテジスト"
    },
    "seo-meta-optimizer": {
        "zh": "SEO 元数据优化专家",
        "ja": "SEO メタ最適化専門家"
    },
    "seo-snippet-hunter": {
        "zh": "SEO 片段搜寻专家",
        "ja": "SEO スニペットハンター"
    },
    "seo-structure-architect": {
        "zh": "SEO 结构架构师",
        "ja": "SEO 構造アーキテクト"
    }
}

def translate_text(text, target_lang):
    """Translate common programming terms and patterns"""
    if not text:
        return text
    
    # If we have a direct translation, use it
    if text.lower() in TRANSLATIONS:
        return TRANSLATIONS[text.lower()].get(target_lang, text)
    
    # Pattern-based translations
    text_lower = text.lower()
    
    if target_lang == "zh":
        # Chinese translations
        if "expert" in text_lower:
            return text.replace("expert", "专家").replace("Expert", "专家")
        elif "developer" in text_lower:
            return text.replace("developer", "开发工程师").replace("Developer", "开发工程师")
        elif "engineer" in text_lower:
            return text.replace("engineer", "工程师").replace("Engineer", "工程师")
        elif "architect" in text_lower:
            return text.replace("architect", "架构师").replace("Architect", "架构师")
        elif "specialist" in text_lower:
            return text.replace("specialist", "专家").replace("Specialist", "专家")
        elif "manager" in text_lower:
            return text.replace("manager", "管理专家").replace("Manager", "管理专家")
    
    elif target_lang == "ja":
        # Japanese translations
        if "expert" in text_lower:
            return text.replace("expert", "エキスパート").replace("Expert", "エキスパート")
        elif "developer" in text_lower:
            return text.replace("developer", "開発者").replace("Developer", "開発者")
        elif "engineer" in text_lower:
            return text.replace("engineer", "エンジニア").replace("Engineer", "エンジニア")
        elif "architect" in text_lower:
            return text.replace("architect", "アーキテクト").replace("Architect", "アーキテクト")
        elif "specialist" in text_lower:
            return text.replace("specialist", "スペシャリスト").replace("Specialist", "スペシャリスト")
        elif "manager" in text_lower:
            return text.replace("manager", "マネージャー").replace("Manager", "マネージャー")
    
    # Return original if no translation found
    return text

def translate_agent_metadata(agent_path):
    """Translate a single agent's metadata"""
    metadata_file = agent_path / "metadata.json"
    if not metadata_file.exists():
        return False
    
    try:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        agent_id = metadata.get('id', '')
        print(f"  [TRANSLATING] {agent_id}")
        
        # Translate name field
        if 'name' in metadata and isinstance(metadata['name'], dict):
            en_name = metadata['name'].get('en', agent_id)
            metadata['name']['zh'] = translate_text(en_name, 'zh')
            metadata['name']['ja'] = translate_text(en_name, 'ja')
        
        # Translate description field  
        if 'description' in metadata and isinstance(metadata['description'], dict):
            en_desc = metadata['description'].get('en', '')
            # For descriptions, we'll keep them in English for now 
            # as they are quite long and complex
            metadata['description']['zh'] = en_desc  # TODO: Translate long descriptions
            metadata['description']['ja'] = en_desc  # TODO: Translate long descriptions
        
        # Translate longDescription field
        if 'longDescription' in metadata and isinstance(metadata['longDescription'], dict):
            en_long_desc = metadata['longDescription'].get('en', '')
            metadata['longDescription']['zh'] = en_long_desc  # TODO: Translate
            metadata['longDescription']['ja'] = en_long_desc  # TODO: Translate
        
        # Save updated metadata
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        print(f"    [SUCCESS] Translated name: {metadata['name']}")
        return True
        
    except Exception as e:
        print(f"    [ERROR] Failed to translate {agent_path}: {e}")
        return False

def translate_all_agents():
    """Translate all agents in the registry"""
    agents_dir = Path("agents")
    if not agents_dir.exists():
        print("[ERROR] agents/ directory not found")
        return
    
    print("Starting translation of agent names...")
    
    translated_count = 0
    error_count = 0
    
    # Iterate through all author directories
    for author_dir in agents_dir.iterdir():
        if not author_dir.is_dir():
            continue
            
        print(f"\n[AUTHOR] Processing: {author_dir.name}")
        
        # Iterate through all agent directories
        for agent_dir in author_dir.iterdir():
            if not agent_dir.is_dir():
                continue
            
            if translate_agent_metadata(agent_dir):
                translated_count += 1
            else:
                error_count += 1
    
    print(f"\n[SUMMARY] Translation completed!")
    print(f"  Successfully translated: {translated_count}")
    print(f"  Errors: {error_count}")
    print(f"  Note: Descriptions kept in English (too complex for auto-translation)")

if __name__ == "__main__":
    # Change to agents-registry directory
    script_dir = Path(__file__).parent
    registry_dir = script_dir.parent
    os.chdir(registry_dir)
    
    translate_all_agents()
