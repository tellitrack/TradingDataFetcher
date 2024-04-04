import asyncio
import telegram
from typing import Optional, Union


class TelegramSender:
    def __init__(self, token):
        print(f"Service Manager for Telegram initialized with token {token}")
        self.bot = telegram.Bot(token=token)

    async def send_message(self,
                           chat_id: Union[int, str],
                           text: str,
                           parse_mode: str = None,
                           disable_web_page_preview: bool = None,
                           disable_notification: bool = None,
                           reply_to_message_id: Optional[int] = None):
        """
        Send a message to a telegram chat.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel.
            text (str): Text of the message to be sent.
            parse_mode (str, optional): Send Markdown or HTML.
            disable_web_page_preview (bool, optional): Disables link previews for links in the message.
            disable_notification (bool, optional): Sends the message silently.
            reply_to_message_id (int, optional): If the message is a reply, ID of the original message.
        """
        await self.bot.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode=telegram.constants.ParseMode.MARKDOWN if parse_mode == "Markdown"
            else telegram.constants.ParseMode.HTML if parse_mode == "HTML" else None,
            disable_web_page_preview=disable_web_page_preview,
            disable_notification=disable_notification,
            reply_to_message_id=reply_to_message_id,
        )

    async def send_document(self,
                            chat_id: Union[int, str],
                            document,
                            caption: Optional[str] = None,
                            parse_mode: str = None,
                            disable_notification: bool = None,
                            reply_to_message_id: Optional[int] = None
                            ):
        """
        Send a document to a chat.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel.
            document: File to send. Can be a file_id, a URL, or a file from the filesystem.
            caption (Optional[str]): Document caption, 0-1024 characters after entities parsing.
            parse_mode (Optional[str]): Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.
            disable_notification (Optional[bool]): Sends the message silently.
            reply_to_message_id (Optional[int]): If the message is a reply, ID of the original message.
        """
        await self.bot.send_document(
            chat_id=chat_id,
            document=document,
            caption=caption,
            parse_mode=telegram.constants.ParseMode.MARKDOWN if parse_mode == "Markdown"
            else telegram.constants.ParseMode.HTML if parse_mode == "HTML" else None,
            disable_notification=disable_notification,
            reply_to_message_id=reply_to_message_id,
        )

    async def send_video(self,
                         chat_id: Union[int, str],
                         video, duration: Optional[int] = None,
                         caption: Optional[str] = None,
                         parse_mode: str = None,
                         disable_notification: bool = None,
                         reply_to_message_id: Optional[int] = None,
                         width: Optional[int] = None,
                         height: Optional[int] = None,
                         supports_streaming: Optional[bool] = None
                         ):
        """
        Send a video to a chat.

        Args:
            chat_id (Union[int, str]): Unique identifier for the target chat or username of the target channel.
            video: Video to send. Can be a file_id, a URL, or a file from the filesystem.
            duration (Optional[int]): Duration of sent video in seconds.
            caption (Optional[str]): Video caption, 0-1024 characters after entities parsing.
            parse_mode (Optional[str]): Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.
            disable_notification (Optional[bool]): Sends the message silently.
            reply_to_message_id (Optional[int]): If the message is a reply, ID of the original message.
            width (Optional[int]): Video width.
            height (Optional[int]): Video height.
            supports_streaming (Optional[bool]): Pass True, if the uploaded video is suitable for streaming.
        """
        await self.bot.send_video(
            chat_id=chat_id,
            video=video,
            duration=duration,
            caption=caption,
            parse_mode=telegram.constants.ParseMode.MARKDOWN if parse_mode == "Markdown"
            else telegram.constants.ParseMode.HTML if parse_mode == "HTML" else None,
            disable_notification=disable_notification,
            reply_to_message_id=reply_to_message_id,
            width=width,
            height=height,
            supports_streaming=supports_streaming
        )

    def send_sync_message(self,
                          chat_id,
                          message,
                          parsing_mode: str = None,
                          **kwargs
                          ):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.send_message(chat_id, message, parsing_mode, **kwargs))

    def send_sync_document(self,
                           chat_id,
                           document,
                           caption=None,
                           parsing_mode=None,
                           **kwargs
                           ):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.send_document(chat_id, document, caption, parsing_mode, **kwargs))

    def send_sync_video(self,
                        chat_id,
                        video,
                        duration=None,
                        caption=None,
                        parse_mode=None,
                        disable_notification=None,
                        reply_to_message_id=None,
                        reply_markup=None,
                        width=None,
                        height=None
                        ):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.send_video(chat_id, video, duration, caption, parse_mode,
                                                disable_notification, reply_to_message_id,
                                                reply_markup, width, height))