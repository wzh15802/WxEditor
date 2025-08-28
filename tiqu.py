import re
import pyperclip
import requests
from PyQt5.QtWidgets import QMessageBox
import json
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import html
import sys
import os

class tiquff:
    def tiqu135sc(self, id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
        }
        response = requests.get('https://www.135editor.com/editor_styles/{}.html'.format(id), headers=headers)
        response.encoding = 'utf-8'
        com = re.compile('<div class="l-img">.*?</div>', re.S)
        shou = com.findall(response.text)
        if shou:
            shou = shou[0]
            pyperclip.copy(shou)
            QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用！')
        else:
            QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')

    def tiqu96ys(self, id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
        }
        response = requests.get('https://bj.96weixin.com/material/style/{}.html'.format(id), headers=headers)
        response.encoding = 'utf-8'
        com = re.compile('<div class="detail_block detail_block_style">.*?</div>', re.S)
        shou = com.findall(response.text)
        if shou:
            shou = shou[0]
            pyperclip.copy(shou)
            QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用！')
        else:
            QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')

    def tiqu96mb(self, id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
        }
        response = requests.get('https://bj.96weixin.com/material/tpl/{}.html'.format(id), headers=headers)
        response.encoding = 'utf-8'
        com = re.compile('<div class="detail_block detail_block_style">.*?</div>', re.S)
        shou = com.findall(response.text)
        if shou:
            shou = shou[0]
            pyperclip.copy(shou)
            QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用！')
        else:
            QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')

    # 用于输入数字id的提取
    def tiqu365sc1(self,target_id):
        current_page = 1
        found = False

        def huoqu365mbf(page):
            url = 'https://www.365editor.com/style/search'
            headers = {
                'User-Agent': 'Origin,DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization'
            }
            fwcs = {
                'page': page,
                'pagesize': 1000,
                'is_vip':'-1',
                'classname':'',
                'tagname':'',
                'keyword': '',
            }
            response = requests.post(url, headers=headers, data=fwcs)
            response.raise_for_status()  # 如果请求不成功，抛出异常
            return json.loads(response.text)

        while True:
            # 获取当前页数据
            data = huoqu365mbf(current_page)

            # 在当前页查找目标 target_id
            for item in data['msg']['data']:
                if item['id'] == target_id:
                    shou = html.unescape(item['code'])
                    if shou:
                        pyperclip.copy(shou)
                        QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用！')
                    else:
                        QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')
                    found = True
                    break

            if found:
                break  # 如果找到了，退出循环

            # 检查是否到达最大页数
            if current_page >= data['msg']['lastpage']:
                break

            # 继续下一页
            current_page += 1

        if not found:
            QMessageBox.information(None, '提示', '获取失败，请检查模板信息是否正确！')
    # 用于输入英文id的提取
    def tiqu365sc2(self,target_id):
        current_page = 1
        found = False

        def huoqu365mbf(page):
            url = 'https://www.365editor.com/style/search'
            headers = {
                'User-Agent': 'Origin,DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization'
            }
            fwcs = {
                'page': page,
                'pagesize': 1000,
                'is_vip': '-1',
                'classname': '',
                'tagname': '',
                'keyword': '',
            }
            response = requests.post(url, headers=headers, data=fwcs)
            response.raise_for_status()  # 如果请求不成功，抛出异常
            return json.loads(response.text)

        while True:
            # 获取当前页数据
            data = huoqu365mbf(current_page)

            # 在当前页查找目标 target_id
            for item in data['msg']['data']:
                if item['encryptionid'] == target_id:
                    shou = html.unescape(item['code'])
                    if shou:
                        pyperclip.copy(shou)
                        QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用！')
                    else:
                        QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')
                    found = True
                    break

            if found:
                break  # 如果找到了，退出循环

            # 检查是否到达最大页数
            if current_page >= data['msg']['lastpage']:
                break

            # 继续下一页
            current_page += 1

        if not found:
            QMessageBox.information(None, '提示', '获取失败，请检查模板信息是否正确！')

    def tiqu365mb1(self,target_id):
        current_page = 1
        found = False

        def huoqu365mbf(page):
            url = 'https://www.365editor.com/template/search'
            headers = {
                'User-Agent': 'Origin,DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization'
            }
            fwcs = {
                'page': page,
                'pagesize': 1000,
                'keyword': '',
            }
            response = requests.post(url, headers=headers, data=fwcs)
            response.raise_for_status()  # 如果请求不成功，抛出异常
            return json.loads(response.text)

        while True:
            # 获取当前页数据
            data = huoqu365mbf(current_page)

            # 在当前页查找目标 target_id
            for item in data['msg']['data']:
                if item['id'] == target_id:
                    shou = html.unescape(item['code'])
                    if shou:
                        pyperclip.copy(shou)
                        QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用！')
                    else:
                        QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')
                    found = True
                    break

            if found:
                break  # 如果找到了，退出循环

            # 检查是否到达最大页数
            if current_page >= data['msg']['lastpage']:
                break

            # 继续下一页
            current_page += 1

        if not found:
            QMessageBox.information(None, '提示', '获取失败，请检查模板信息是否正确！')

    def tiqu365mb2(self, target_id):
        current_page = 1
        found = False

        def huoqu365mbf(page):
            url = 'https://www.365editor.com/template/search'
            headers = {
                'User-Agent': 'Origin,DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization'
            }
            fwcs = {
                'page': page,
                'pagesize': 1000,
                'keyword': '',
            }
            response = requests.post(url, headers=headers, data=fwcs)
            response.raise_for_status()  # 如果请求不成功，抛出异常
            return json.loads(response.text)

        while True:
            # 获取当前页数据
            data = huoqu365mbf(current_page)
            # 在当前页查找目标 target_id
            for item in data['msg']['data']:
                if item['encryptionid'] == target_id:
                    shou = html.unescape(item['code'])
                    if shou:
                        pyperclip.copy(shou)
                        QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用！')
                    else:
                        QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')
                    found = True
                    break

            if found:
                break  # 如果找到了，退出循环

            # 检查是否到达最大页数
            if current_page >= data['msg']['lastpage']:
                break

            # 继续下一页
            current_page += 1

        if not found:
            QMessageBox.information(None, '提示', '获取失败，请检查模板信息是否正确！')

    def tiqumyys(self,id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
        }
        response = requests.get('https://www.xmyeditor.com/styleinfo/{}.html'.format(id), headers=headers)
        response.encoding = 'utf-8'
        # com = re.compile('<div class="XQ01-mine">.*?</div>', re.S)
        #shou = com.findall(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        shou = soup.find('div', attrs={'data-id': str(id)})

        if shou:
            #shou = shou[0]
            pyperclip.copy(str(shou))
            QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用(必须使用135编辑器粘贴)！')
        else:
            QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')

    def tiqumyqw(self, id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
        }
        response = requests.get(f'https://www.xmyeditor.com/tplinfo/{id}.html', headers=headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        shou = soup.find('div', class_='XQ02-mine')

        if shou:
            xmy_background = shou.find('div', id='xmyBackground')  # 继续查找目标 div
            if xmy_background:
                pyperclip.copy(str(xmy_background))  # 复制目标 div 的 HTML 代码
                QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用(必须使用135编辑器粘贴)！')
            else:
                QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')
        else:
            QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')

    # 主编元素
    def tiquzbys(self,id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
        }
        response = requests.get('https://www.zhubian.com/material/style/{}.html'.format(id), headers=headers)
        response.encoding = 'utf-8'
        com = re.compile('<div class="detail_block detail_block_style">.*?</div>', re.S)
        shou = com.findall(response.text)
        if shou:
            shou = shou[0]
            pyperclip.copy(shou)
            QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用！')
        else:
            QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')

    # 主编-模板
    def tiquzbmb(self,id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
        }
        response = requests.get('https://www.zhubian.com/material/tpl/{}.html'.format(id), headers=headers)
        response.encoding = 'utf-8'
        com = re.compile('<div class="detail_block detail_block_style">.*?</div>', re.S)
        shou = com.findall(response.text)
        if shou:
            shou = shou[0]
            pyperclip.copy(shou)
            QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用！')
        else:
            QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')

    # 壹伴-元素
    def tiquybys(self,id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
        }
        response = requests.get('https://yiban.io/api/article_editor/material/one?material_id={}'.format(id), headers=headers)
        response.encoding = 'utf-8'
        data = json.loads(response.text)
        if 'material' in data and 'detail' in data['material']:
            # 提取HTML代码
            html_code = data['material']['detail']
            # 将转义字符还原为实际的特殊字符
            shou = html.unescape(html_code)
            if shou:
                pyperclip.copy(shou)
                QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用！')
            else:
                QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')
        else:
            QMessageBox.information(None, '提示', '获取失败，请检查模板ID信息是否正确！')

    # 壹伴-模板
    def tiquybmb(self,id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
        }
        response = requests.get('https://yiban.io/api/style_template/system/one?style_template_id={}'.format(id),
                                headers=headers)
        response.encoding = 'utf-8'
        data = json.loads(response.text)
        if 'style_template' in data and 'total' in data['style_template']:
            total = data['style_template']['total']
            shou = html.unescape(total)
            if shou:
                pyperclip.copy(shou)
                QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用！')
            else:
                QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')
        else:
            QMessageBox.information(None, '提示', '获取失败，请检查模板ID信息是否正确！')

    # 易点-元素
    def tiquydys(self,id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
        }
        response = requests.get('https://www.wxeditor.com/showMaterial/id/{}'.format(id), headers=headers)
        response.encoding = 'utf-8'
        com = re.compile('<div class="wd">.*?</div>', re.S)
        shou = com.findall(response.text)
        if shou:
            shou = shou[0]
            pyperclip.copy(shou)
            QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用！')
        else:
            QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')

    # 易点-模板
    def tiquydmb(self,id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
        }
        response = requests.get('https://www.wxeditor.com/preview/type/template/id/{}'.format(id), headers=headers)
        response.encoding = 'utf-8'
        com = re.compile('<div id="preview" class="rich_media_content">.*?</div>', re.S)
        shou = com.findall(response.text)
        if shou:
            shou = shou[0]
            pyperclip.copy(shou)
            QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用！')
        else:
            QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')

    # 秀米-风格排版
    def xiumiyulan(self,id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
        }
        url = f'https://xiumi.us/api/show_goods/goodses/{id}'  # 使用 f-string 插入 ID

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # 自动检查 HTTP 错误码（如 404、500）

            # 解析并打印 JSON
            data = response.json()
            showurl = data['data']['show']['show_url']
            print(showurl)
            # 抓取源码
            start_time = time.time()
            with sync_playwright() as p:
                # 动态获取路径（兼容打包后的临时目录）
                base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
                browser_path = os.path.join(base_path,
                                            "ms-playwright/chromium_headless_shell-1161/chrome-win/headless_shell.exe")
                # 启动优化配置（兼容旧版本）
                browser = p.chromium.launch(
                    headless=True,
                    executable_path=browser_path,
                    args=[
                        "--single-process",
                        "--disable-images",
                        "--no-sandbox",
                        "--aggressive-cache-discard"
                    ],
                    timeout=10_000
                )

                # 创建上下文（移除非必要参数）
                context = browser.new_context(
                    bypass_csp=True,
                    # 使用新版 initial_scripts 替代旧版 scripts（需Playwright>=1.32）
                    # initial_scripts=[{"content": "window.__optimized = true;"}]
                )

                page = context.new_page()

                try:
                    # 资源拦截加速
                    def route_handler(route):
                        blocked = [
                            "image", "stylesheet", "font",
                            "media", "other"
                        ]
                        if route.request.resource_type in blocked:
                            route.abort()
                        else:
                            route.continue_()

                    page.route("**/*", route_handler)

                    # 复合导航策略
                    page.goto(showurl, wait_until="commit", timeout=5000)
                    page.wait_for_load_state("domcontentloaded")

                    # 精确选择器（兼容Angular属性）
                    selector = 'div.row.tn-article-body.tn-opera-house.display-system-page-margins'
                    page.wait_for_selector(selector, state="visible", timeout=2000)

                    # 高效获取源码
                    target_div = page.eval_on_selector(selector, "el => el.outerHTML")

                    if target_div:
                        def fix_xiumi_urls(html_content):
                            """直接替换所有协议相对路径为https"""
                            """处理秀米URL协议及OSS参数问题"""
                            # 协议相对路径处理
                            processed_html = re.sub(
                                r'(?<!https:)//img\.xiumi\.us',
                                'https://img.xiumi.us',
                                html_content,
                                flags=re.IGNORECASE
                            )
                            processed_html = re.sub(
                                r'(?<!http:)//statics\.xiumi\.us',
                                'http://statics.xiumi.us',
                                processed_html,
                                flags=re.IGNORECASE
                            )

                            # 精准移除x-oss-process参数（支持多种场景）
                            processed_html = re.sub(
                                r'(https?://(?:img|statics)\.xiumi\.us/[^\s"\'<>?]+)(?:\?x-oss-process=[^&"\')\s>]*)',
                                r'\1',
                                processed_html,
                                flags=re.IGNORECASE
                            )
                            return processed_html

                        processed_html = fix_xiumi_urls(target_div)
                        pyperclip.copy(processed_html)
                        QMessageBox.information(None, '提示', '提取成功，请在微信编辑器源码模式中粘贴使用！')
                    else:
                        print("元素不存在")
                        QMessageBox.information(None, '提示', '提取失败，请检查模板信息是否正确！')

                    return target_div

                except Exception as e:
                    print(f"抓取失败: {str(e)}")
                    QMessageBox.information(None, '提示', '抓取失败，请检查模板信息是否正确！')
                    return None

                finally:
                    context.close()

        except requests.exceptions.RequestException as e:
            print(f"请求出错：{e}")
            QMessageBox.information(None, '提示', '数据请求出错，暂时无法获取！')
        except ValueError:
            print("响应内容不是有效 JSON")
            QMessageBox.information(None, '提示', 'json数据请求出错，暂时无法获取！')
