// /event/:slug/
const permalink = ({ page: { fileSlug } }) => `/event/${fileSlug}/`;

export default {
  layout: "event",
  permalink,
  tags: "events",
};
