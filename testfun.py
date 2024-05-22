
import asyncio
import traceback

from telegram_upload.client import TelegramManagerClient
# from telegram_upload.files import NoDirectoriesFiles, RecursiveFiles, NoLargeFiles, SplitFiles, is_valid_file
from telegram_upload.upload_files import NoDirectoriesFiles, RecursiveFiles, NoLargeFiles, SplitFiles, is_valid_file
DIRECTORY_MODES = {
    'fail': NoDirectoriesFiles,
    'recursive': RecursiveFiles,
}
LARGE_FILE_MODES = {
    'fail': NoLargeFiles,
    'split': SplitFiles,
}
def tgupload(files, to, quchu, vif, nobar, dzffn, config, c1, delete_on_success, print_file_id, force_file, forward, directories, large_files, caption, c2,no_thumbnail, thumbnail_file, proxy, album):
    """Upload one or more files to dxdmgch using your personal account.
    The maximum file size is 2 GiB and by default they will be saved in
    your saved messages.
    """
    # print('upload({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {},{}, {}, {}, {})'.format(files, to, quchu, vif, nobar, dzffn, config, c1, delete_on_success, print_file_id, force_file, forward, directories, large_files, caption, c2,no_thumbnail, thumbnail_file, proxy, album))
    try:
        if c1 is not None:
            config = c1
        if c2 is not None:
            caption = c2
        if quchu != 'me':
            to = quchu
        client = TelegramManagerClient(config or default_config(), proxy=proxy)
        client.start()
        files = filter(lambda file: is_valid_file(file, lambda message: click.echo(message, err=True)), files)
        files = DIRECTORY_MODES[directories](client, files)
        if directories == 'fail':
            # Validate now
            files = list(files)
        if no_thumbnail:
            thumbnail = False
        elif thumbnail_file:
            thumbnail = thumbnail_file
        else:
            thumbnail = None
        files_cls = LARGE_FILE_MODES[large_files]
        files = files_cls(client, files, caption=caption, thumbnail=thumbnail, force_file=force_file, dzffn=dzffn)
        if large_files == 'fail':
            # Validate now
            files = list(files)
        if isinstance(to, str) and to.lstrip("-+").isdigit():
            to = int(to)
        if album:
            client.send_files_as_album(to, vif, nobar, files, delete_on_success, print_file_id, forward)
        else:
            print('print(files): {}'.format(files))
            client.send_files(to, vif, nobar, files, delete_on_success, print_file_id, forward)
        client.disconnect()
    except Exception as e:
        traceback.print_exc()
        client.disconnect()


file_path = ['/workspaces/telegram-uploaddzb/2023_05_09_16_27_35.dox']
to_cha='-1002113604998'
vif=True
nobar=False
# 定制 ffmpeg
dzffn = 'ffmpeg'
config_path = '/home/codespace/.config/telegram-upload.json'
caption = '卖车美女_重庆银马_长安马自达重庆银马店_2024-05-22-21-10-06_Herokuxxxx_Douyin_douyinzhibo37xby_0'
new_loop = asyncio.new_event_loop()
asyncio.set_event_loop(new_loop)
tgupload(files=file_path, to=to_cha, quchu='me', vif=vif, nobar=nobar, dzffn=dzffn, config=config_path, c1=None, delete_on_success=True, 
            print_file_id=False, force_file=False, forward=(), directories='fail', large_files='fail', caption=caption, c2=None,no_thumbnail=False, 
            thumbnail_file=None, proxy=None, album=False)