--
-- PostgreSQL database dump
--

-- Dumped from database version 12.11 (Ubuntu 12.11-1.pgdg20.04+1)
-- Dumped by pg_dump version 12.11 (Ubuntu 12.11-1.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: shifts; Type: TABLE; Schema: public; Owner: auxil
--

CREATE TABLE public.shifts (
    shiftstart timestamp with time zone NOT NULL,
    shiftdate date,
    shift integer,
    crew text,
    prettyname text,
    length integer,
    shiftstart_epoch bigint
);


ALTER TABLE public.shifts OWNER TO auxil;

--
-- Data for Name: shifts; Type: TABLE DATA; Schema: public; Owner: auxil
--

COPY public.shifts (shiftstart, shiftdate, shift, crew, prettyname, length, shiftstart_epoch) FROM stdin;
2022-05-11 16:00:00+03	2022-05-11	3	C	2022-05-11 3	28800	1652274000
2022-05-12 00:00:00+03	2022-05-12	1	D	2022-05-12 1	28800	1652302800
2022-05-12 08:00:00+03	2022-05-12	2	A	2022-05-12 2	28800	1652331600
2022-05-12 16:00:00+03	2022-05-12	3	C	2022-05-12 3	28800	1652360400
2022-05-13 00:00:00+03	2022-05-13	1	D	2022-05-13 1	28800	1652389200
2022-05-13 08:00:00+03	2022-05-13	2	A	2022-05-13 2	28800	1652418000
2022-05-13 16:00:00+03	2022-05-13	3	B	2022-05-13 3	28800	1652446800
2022-05-14 00:00:00+03	2022-05-14	1	D	2022-05-14 1	28800	1652475600
2022-05-14 08:00:00+03	2022-05-14	2	A	2022-05-14 2	28800	1652504400
2022-05-14 16:00:00+03	2022-05-14	3	B	2022-05-14 3	28800	1652533200
2022-05-15 00:00:00+03	2022-05-15	1	C	2022-05-15 1	28800	1652562000
2022-05-15 08:00:00+03	2022-05-15	2	A	2022-05-15 2	28800	1652590800
2022-05-15 16:00:00+03	2022-05-15	3	B	2022-05-15 3	28800	1652619600
2022-05-16 00:00:00+03	2022-05-16	1	C	2022-05-16 1	28800	1652648400
2022-05-16 08:00:00+03	2022-05-16	2	A	2022-05-16 2	28800	1652677200
2022-05-16 16:00:00+03	2022-05-16	3	B	2022-05-16 3	28800	1652706000
2022-05-17 00:00:00+03	2022-05-17	1	C	2022-05-17 1	28800	1652734800
2022-05-17 08:00:00+03	2022-05-17	2	D	2022-05-17 2	28800	1652763600
2022-05-17 16:00:00+03	2022-05-17	3	B	2022-05-17 3	28800	1652792400
2022-05-18 00:00:00+03	2022-05-18	1	C	2022-05-18 1	28800	1652821200
2022-05-18 08:00:00+03	2022-05-18	2	D	2022-05-18 2	28800	1652850000
2022-05-18 16:00:00+03	2022-05-18	3	B	2022-05-18 3	28800	1652878800
2022-05-19 00:00:00+03	2022-05-19	1	C	2022-05-19 1	28800	1652907600
2022-05-19 08:00:00+03	2022-05-19	2	D	2022-05-19 2	28800	1652936400
2022-05-19 16:00:00+03	2022-05-19	3	A	2022-05-19 3	28800	1652965200
2022-05-20 00:00:00+03	2022-05-20	1	C	2022-05-20 1	28800	1652994000
2022-05-20 08:00:00+03	2022-05-20	2	D	2022-05-20 2	28800	1653022800
2022-05-20 16:00:00+03	2022-05-20	3	A	2022-05-20 3	28800	1653051600
2022-05-21 00:00:00+03	2022-05-21	1	B	2022-05-21 1	28800	1653080400
2022-05-21 08:00:00+03	2022-05-21	2	D	2022-05-21 2	28800	1653109200
2022-05-21 16:00:00+03	2022-05-21	3	A	2022-05-21 3	28800	1653138000
2022-05-22 00:00:00+03	2022-05-22	1	B	2022-05-22 1	28800	1653166800
2022-05-22 08:00:00+03	2022-05-22	2	D	2022-05-22 2	28800	1653195600
\.


--
-- Name: shifts shifts_pkey; Type: CONSTRAINT; Schema: public; Owner: auxil
--

ALTER TABLE ONLY public.shifts
    ADD CONSTRAINT shifts_pkey PRIMARY KEY (shiftstart);


--
-- Name: shiftstart cluster; Type: INDEX; Schema: public; Owner: auxil
--

CREATE INDEX "shiftstart cluster" ON public.shifts USING btree (shiftstart);

ALTER TABLE public.shifts CLUSTER ON "shiftstart cluster";


--
-- Name: shiftstart_epoch; Type: INDEX; Schema: public; Owner: auxil
--

CREATE INDEX shiftstart_epoch ON public.shifts USING btree (shiftstart_epoch);


--
-- PostgreSQL database dump complete
--

