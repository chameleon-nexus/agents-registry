#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple import script for agents-main
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path

def parse_agent_frontmatter(content):
    """Parse agent frontmatter"""
    if not content.startswith('---'):
        return None, content
    
    try:
        end_idx = content.find('---', 3)
        if end_idx == -1:
            return None, content
            
        frontmatter_text = content[3:end_idx].strip()
        body = content[end_idx + 3:].strip()
        
        frontmatter = {}
        for line in frontmatter_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip('"\'')
                
                if key == 'tools' and ',' in value:
                    frontmatter[key] = [t.strip() for t in value.split(',')]
                else:
                    frontmatter[key] = value
                    
        return frontmatter, body
    except Exception as e:
        print(f"Parse error: {e}")
        return None, content

def infer_category_from_content(name, description, tools, content):
    """Infer category from content"""
    text = f"{name} {description} {' '.join(tools or [])} {content}".lower()
    
    if any(word in text for word in ['debug', 'error', 'bug', 'troubleshoot', 'fix']):
        return 'debugging'
    elif any(word in text for word in ['data', 'analysis', 'sql', 'chart', 'statistics']):
        return 'data'
    elif any(word in text for word in ['document', 'readme', 'doc', 'comment']):
        return 'documentation'
    elif any(word in text for word in ['test', 'unit', 'integration', 'quality', 'review']):
        return 'development'
    else:
        return 'development'

def convert_agent(agent_file_path):
    """Convert single agent file"""
    try:
        with open(agent_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        print(f"Failed to read: {agent_file_path}")
        return None
    
    frontmatter, body = parse_agent_frontmatter(content)
    if not frontmatter:
        print(f"No frontmatter: {agent_file_path}")
        return None
    
    # Generate agent ID
    agent_id = frontmatter.get('name', '').lower().replace(' ', '-').replace('_', '-')
    agent_id = re.sub(r'[^a-z0-9\-]', '', agent_id)
    
    if not agent_id:
        print(f"No agent ID: {agent_file_path}")
        return None
    
    # Infer category
    category = infer_category_from_content(
        frontmatter.get('name', ''),
        frontmatter.get('description', ''),
        frontmatter.get('tools', []),
        body
    )
    
    # Generate tags
    tags = []
    if frontmatter.get('tools'):
        tags.extend(frontmatter['tools'])
    
    description = frontmatter.get('description', '').lower()
    if 'typescript' in description or 'ts' in description:
        tags.append('typescript')
    if 'javascript' in description or 'js' in description:
        tags.append('javascript')
    if 'python' in description:
        tags.append('python')
    if 'security' in description:
        tags.append('security')
    if 'review' in description:
        tags.append('code-review')
    
    tags = list(set(tags))
    
    # Create metadata
    metadata = {
        "id": agent_id,
        "name": {
            "en": frontmatter.get('name', agent_id.title()),
            "zh": frontmatter.get('name', agent_id.title())
        },
        "description": {
            "en": frontmatter.get('description', ''),
            "zh": frontmatter.get('description', '')
        },
        "longDescription": {
            "en": body[:200] + "..." if len(body) > 200 else body,
            "zh": body[:200] + "..." if len(body) > 200 else body
        },
        "author": "Community",
        "license": "MIT",
        "homepage": "https://github.com/chameleon-nexus/agents-registry",
        "category": category,
        "tags": tags,
        "compatibility": {
            "claudeCode": {
                "minVersion": "1.0.0",
                "tested": ["1.0.0"]
            }
        },
        "versions": {
            "1.0.0": {
                "releaseDate": datetime.now().isoformat() + "Z",
                "changes": "Imported from agents-main project",
                "files": {
                    "agent": "agent.md"
                }
            }
        },
        "latest": "1.0.0",
        "downloads": 0,
        "rating": 0,
        "ratingCount": 0,
        "createdAt": datetime.now().isoformat() + "Z",
        "updatedAt": datetime.now().isoformat() + "Z"
    }
    
    return {
        "id": agent_id,
        "metadata": metadata,
        "content": content
    }

def main():
    """Main function"""
    agents_main_dir = "agents-main"
    output_dir = "agents"
    
    if not os.path.exists(agents_main_dir):
        print(f"Error: {agents_main_dir} not found")
        return
    
    os.makedirs(output_dir, exist_ok=True)
    
    converted_agents = {}
    
    # Process .md files
    for md_file in Path(agents_main_dir).glob("*.md"):
        if md_file.name in ["README.md", "AGENTS.md"]:
            continue
            
        print(f"Processing: {md_file}")
        agent_data = convert_agent(md_file)
        
        if agent_data:
            agent_id = agent_data["id"]
            
            # Create agent directory
            agent_dir = os.path.join(output_dir, "community", agent_id)
            os.makedirs(agent_dir, exist_ok=True)
            
            # Save metadata
            with open(os.path.join(agent_dir, "metadata.json"), 'w', encoding='utf-8') as f:
                json.dump(agent_data["metadata"], f, indent=2, ensure_ascii=False)
            
            # Save agent content
            with open(os.path.join(agent_dir, "agent.md"), 'w', encoding='utf-8') as f:
                f.write(agent_data["content"])
            
            # Add to registry
            converted_agents[agent_id] = {
                "name": agent_data["metadata"]["name"],
                "description": agent_data["metadata"]["description"],
                "author": agent_data["metadata"]["author"],
                "category": agent_data["metadata"]["category"],
                "tags": agent_data["metadata"]["tags"],
                "latest": agent_data["metadata"]["latest"],
                "versions": list(agent_data["metadata"]["versions"].keys()),
                "downloads": 0,
                "rating": 0,
                "ratingCount": 0,
                "license": agent_data["metadata"]["license"],
                "compatibility": agent_data["metadata"]["compatibility"],
                "createdAt": agent_data["metadata"]["createdAt"],
                "updatedAt": agent_data["metadata"]["updatedAt"]
            }
            
            print(f"SUCCESS: {agent_id}")
        else:
            print(f"FAILED: {md_file}")
    
    # Generate registry.json
    categories = {
        "development": {
            "en": "Code Development",
            "zh": "代码开发",
            "description": {
                "en": "Agents for coding, refactoring, and code quality",
                "zh": "用于编码、重构和代码质量的代理"
            },
            "icon": "💻"
        },
        "debugging": {
            "en": "Problem Solving",
            "zh": "问题排查",
            "description": {
                "en": "Agents for debugging and troubleshooting", 
                "zh": "用于调试和故障排除的代理"
            },
            "icon": "🐛"
        },
        "data": {
            "en": "Data & Analytics",
            "zh": "数据分析",
            "description": {
                "en": "Agents for data analysis and processing",
                "zh": "用于数据分析和处理的代理"
            },
            "icon": "📊"
        },
        "documentation": {
            "en": "Documentation",
            "zh": "文档编写",
            "description": {
                "en": "Agents for writing and maintaining documentation",
                "zh": "用于编写和维护文档的代理"
            },
            "icon": "📝"
        }
    }
    
    registry = {
        "version": "1.0.0",
        "lastUpdated": datetime.now().isoformat() + "Z",
        "totalAgents": len(converted_agents),
        "agents": converted_agents,
        "categories": categories,
        "stats": {
            "totalDownloads": 0,
            "activeUsers": 0,
            "topAgents": list(converted_agents.keys())[:10],
            "recentUpdates": []
        }
    }
    
    with open("registry.json", 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
    
    print(f"\nConversion complete!")
    print(f"Total converted: {len(converted_agents)} agents")
    print(f"Output directory: {output_dir}")
    print(f"Registry: registry.json")

if __name__ == "__main__":
    main()
